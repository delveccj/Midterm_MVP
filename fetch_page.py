import requests

def fetch_website_content(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "https://example.com"
    content = fetch_website_content(url)
    print(content[:100])  # Print only the first 100 characters
