import sys
import asyncio

from asynccrawler import crawl_site_async

async def main():
    if len(sys.argv) != 4:
        print(
            "usage: uv run main.py URL max_concurrency max_pages"
        )
        sys.exit(1)

    base_url = sys.argv[1]
    max_concurrency = int(sys.argv[2])
    max_pages = int(sys.argv[3])

    print(f"starting crawl of: {base_url}")

    page_data = await crawl_site_async(
        base_url,
        max_concurrency=max_concurrency,
        max_pages=max_pages,
    )

    print(f"\nFound {len(page_data)} pages\n")

    for data in page_data.values():
        print(f"URL: {base_url}")
        print(f"Heading: {data['heading']}")
        print(f"Links: {len(data['outgoing_links'])}")
        print(f"Images: {len(data['image_urls'])}")
        print()


if __name__ == "__main__":
    asyncio.run(main())
