import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # ❌ Remove unwanted tags
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    # ✅ Target main content (important for GFG)
    article = soup.find("article")

    if article:
        text = article.get_text(separator="\n")
    else:
        text = soup.get_text(separator="\n")

    return text