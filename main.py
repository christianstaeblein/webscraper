from crawl import get_heading_from_html

def main():
    print("Hello from web-scraper!")
    print(get_heading_from_html("""<html>
      <body>
        <h1>Welcome to Boot.dev</h1>
        <main>
          <h2>Getting Started<h2>
          <p>Learn to code by building real projects.</p>
          <p>This is the second paragraph.</p>
        </main>
      </body>
    </html>"""))

if __name__ == "__main__":
    main()
