import sys
from crawl import get_html
from crawl import crawl_page

def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)

    base_url = sys.argv[1]

    print(f"starting crawl of: {base_url}")

    page_data = crawl_page(base_url)

    print(f"\nFound {len(page_data)} pages\n")

    for url, data in page_data.items():
        print(f"URL: {url}")
        print(f"Heading: {data['heading']}")
        print(f"Links: {len(data['outgoing_links'])}")
        print(f"Images: {len(data['image_urls'])}")
        print()


if __name__ == "__main__":
    main()
