import asyncio
import aiohttp

from urllib.parse import urlsplit

from crawl import (
    normalize_url,
    extract_page_data,
)


class AsyncCrawler:
    def __init__(self, base_url, max_concurrency=5):
        self.base_url = base_url
        self.base_domain = urlsplit(base_url).netloc

        self.page_data = {}
        self.visited = set()

        self.lock = asyncio.Lock()

        self.max_concurrency = max_concurrency
        self.semaphore = asyncio.Semaphore(max_concurrency)

        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            headers={"User-Agent": "BootCrawler/1.0"}
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def add_page_visit(self, normalized_url):
        async with self.lock:
            if normalized_url in self.visited:
                return False

            self.visited.add(normalized_url)
            return True

    async def get_html(self, url):
        try:
            async with self.session.get(url) as response:
                response.raise_for_status()

                content_type = response.headers.get(
                    "content-type", ""
                )

                if "text/html" not in content_type:
                    raise Exception(f"invalid content type: {content_type}")

                return await response.text()

        except Exception:
            raise

    async def crawl_page(self, current_url):
        # same-domain check
        if urlsplit(current_url).netloc != self.base_domain:
            return

        normalized_url = normalize_url(current_url)

        # Don't crawl the same page twice
        is_new_page = await self.add_page_visit(
            normalized_url
        )

        if not is_new_page:
            return

        print(f"Crawling: {current_url}")

        async with self.semaphore:
            try:
                html = await self.get_html(current_url)
            except Exception as e:
                print(
                    f"Error crawling {current_url}: {e}"
                )
                return

        data = extract_page_data(html, current_url)

        async with self.lock:
            self.page_data[normalized_url] = data

        tasks = []

        for url in data["outgoing_links"]:
            tasks.append(
                asyncio.create_task(
                    self.crawl_page(url)
                )
            )

        if tasks:
            await asyncio.gather(*tasks)

    async def crawl(self):
        await self.crawl_page(self.base_url)
        return self.page_data


async def crawl_site_async(
    base_url,
    max_concurrency=5,
):
    async with AsyncCrawler(
        base_url,
        max_concurrency=max_concurrency,
    ) as crawler:
        return await crawler.crawl()
