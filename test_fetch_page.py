import unittest
from fetch_page import fetch_website_content

class TestFetchPage(unittest.TestCase):
    def test_fetch_website_content(self):
        content = fetch_website_content("https://example.com")
        self.assertIn("<h1>Example Domain</h1>", content)  # This will fail initially

if __name__ == "__main__":
    unittest.main()
