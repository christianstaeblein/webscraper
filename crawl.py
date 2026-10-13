from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag

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
