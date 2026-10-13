from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag
from urllib.parse import urljoin
from urllib.parse import urlsplit
import requests

def normalize_url(url:str)->str:
    norm=urlsplit(url)
    norm=f"{norm.netloc}{norm.path}"
    return norm if norm[-1]!="/" else norm[:-1]

def get_heading_from_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')

    if soup.h1 is not None:
        return soup.h1.get_text()
    elif soup.h2 is not None:
        return soup.h2.get_text()
    else:
        return ""

def get_first_paragraph_from_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')

    if soup.p is not None:
        return soup.p.get_text()
    else:
        return ""

def get_urls_from_html(html: str, base_url: str):
    soup = BeautifulSoup(html, "html.parser")

    urls = []

    for link in soup.find_all("a", href=True):
        href = link.get("href")

        # Skip anchors, JavaScript links, and email links
        if href.startswith(("#", "javascript:", "mailto:")):
            continue

        urls.append(urljoin(base_url, href))

    return urls

def get_images_from_html(html, base_url):
    images = []

    soup = BeautifulSoup(html, "html.parser")

    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue

        images.append(urljoin(base_url, src))

    return images


def extract_page_data(body:str, url:str):

    return {
        "url": url,
        "heading": get_heading_from_html(body),
        "first_paragraph": get_first_paragraph_from_html(body),
        "outgoing_links": get_urls_from_html(body, url),
        "image_urls": get_images_from_html(body, url),
    }


def get_html(url):
    response = requests.get(
        url,
        headers={"User-Agent": "BootCrawler/1.0"}
    )

    response.raise_for_status()

    content_type = response.headers.get("content-type", "")
    if "text/html" not in content_type:
        raise Exception(f"invalid content type: {content_type}")

    return response.text


def crawl_page(base_url, current_url=None, page_data=None):
    if current_url is None:
        current_url = base_url

    if page_data is None:
        page_data = {}

    # Only crawl pages on the same domain
    if urlsplit(current_url).netloc != urlsplit(base_url).netloc:
        return page_data

    normalized_url = normalize_url(current_url)

    # Don't crawl the same page twice
    if normalized_url in page_data:
        return page_data

    print(f"Crawling: {current_url}")

    try:
        html = get_html(current_url)
    except Exception as e:
        print(f"Error crawling {current_url}: {e}")
        return page_data

    data = extract_page_data(html, current_url)
    page_data[normalized_url] = data

    for url in data["outgoing_links"]:
        crawl_page(base_url, url, page_data)

    return page_data
