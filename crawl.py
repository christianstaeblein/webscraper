from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag
from urllib.parse import urljoin

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


from bs4 import BeautifulSoup
from urllib.parse import urljoin


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
