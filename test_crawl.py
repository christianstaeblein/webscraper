import unittest
from crawl import normalize_url
from crawl import get_heading_from_html
from crawl import get_first_paragraph_from_html
from crawl import get_urls_from_html
from crawl import get_images_from_html


class TestCrawl(unittest.TestCase):
    def test_normalize_url_correct(self):
        input_url = "www.boot.dev/blog/path"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_https(self):
        input_url = "https://www.boot.dev/blog/path"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_https_slash(self):
        input_url = "https://www.boot.dev/blog/path/"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_http(self):
        input_url = "http://www.boot.dev/blog/path"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_http_slash(self):
        input_url = "http://www.boot.dev/blog/path/"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_no_http(self):
        input_url = "www.boot.dev/blog/path"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_no_http_slash(self):
        input_url = "www.boot.dev/blog/path/"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_only_h1(self):
        html = """<html>
          <body>
            <h1>Welcome to Boot.dev</h1>
            <main>
              <p>Learn to code by building real projects.</p>
              <p>This is the second paragraph.</p>
            </main>
          </body>
        </html>"""
        actual = get_heading_from_html(html)
        expected = "Welcome to Boot.dev"
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_only_h1_h2(self):
        html = """<html>
          <body>
            <h1>Welcome to Boot.dev</h1>
            <main>
              <h2>Getting Started</h2>
              <p>Learn to code by building real projects.</p>
              <p>This is the second paragraph.</p>
            </main>
          </body>
        </html>"""
        actual = get_heading_from_html(html)
        expected = "Welcome to Boot.dev"
        self.assertEqual(actual, expected)


    def test_get_heading_from_html_only_no_h1_h2(self):
        html = """<html>
          <body>
            <main>
              <h2>Getting Started</h2>
              <p>Learn to code by building real projects.</p>
              <p>This is the second paragraph.</p>
            </main>
          </body>
        </html>"""
        actual = get_heading_from_html(html)
        expected = "Getting Started"
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_only_no_h1_no_h2(self):
        html = """<html>
          <body>
            <main>
              <p>Learn to code by building real projects.</p>
              <p>This is the second paragraph.</p>
            </main>
          </body>
        </html>"""
        actual = get_heading_from_html(html)
        expected = ""
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html(self):
        html = """
        <html>
            <body>
                <p>Hello world.</p>
            </body>
        </html>
        """
        actual = get_first_paragraph_from_html(html)
        expected = "Hello world."
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_multi_p(self):
        html="""<html>
          <body>
            <main>
              <p>Learn to code by building real projects.</p>
              <p>This is the second paragraph.</p>
            </main>
          </body>
        </html>"""
        actual = get_first_paragraph_from_html(html)
        expected = "Learn to code by building real projects."
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_multi_p(self):
        html="""<html>
            <body>
                <h1>Heading</h1>
            <main>
            </main>
            </body>
        </html>"""
        actual = get_first_paragraph_from_html(html)
        expected = ""
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_relative(self):
        input_url = "https://blog.boot.dev"
        input_body = """
        <html>
            <body>
                <a href="/about">About</a>
            </body>
        </html>
        """

        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev/about"]

        self.assertEqual(actual, expected)

    def test_get_urls_from_html_multiple_links(self):
        input_url = "https://blog.boot.dev"
        input_body = """
        <html>
            <body>
                 <a href="/about">About</a>
                 <a href="/contact">Contact</a>
                 <a href="https://blog.boot.dev/pricing">Pricing</a>
            </body>
        </html>
        """

        actual = get_urls_from_html(input_body, input_url)
        expected = [
            "https://blog.boot.dev/about",
            "https://blog.boot.dev/contact",
            "https://blog.boot.dev/pricing",
        ]

        self.assertEqual(actual, expected)

    def test_get_images_from_html_relative(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="/logo.png"></img></body></html>'

        actual = get_images_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/logo.png"]

        self.assertEqual(actual, expected)

    def test_get_images_from_html_absolute(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="https://cdn.example.com/logo.png"></img></body></html>'

        actual = get_images_from_html(input_body, input_url)
        expected = ["https://cdn.example.com/logo.png"]

        self.assertEqual(actual, expected)

    def test_get_images_from_html_missing_src(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img alt="logo"></img></body></html>'

        actual = get_images_from_html(input_body, input_url)
        expected = []

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
