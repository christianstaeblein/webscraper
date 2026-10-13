from urllib.parse import urlsplit

def normalize_url(url:str)->str:
    print(urlsplit(url))
    norm=urlsplit(url)
    norm=f"{norm.netloc}{norm.path}"
    return norm if norm[-1]!="/" else norm[:-1]
