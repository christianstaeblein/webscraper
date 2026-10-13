import unittest
from crawl import normalize_url
from crawl import get_heading_from_html
from crawl import get_first_paragraph_from_html


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

if __name__ == "__main__":
    unittest.main()
