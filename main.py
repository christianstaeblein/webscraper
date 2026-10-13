import sys
from crawl import normalize_url
from crawl import get_heading_from_html
from crawl import get_first_paragraph_from_html
from crawl import get_urls_from_html
from crawl import get_images_from_html
from crawl import extract_page_data

def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)

    base_url = sys.argv[1]
    print(f"starting crawl of: {base_url}")


if __name__ == "__main__":
    main()
