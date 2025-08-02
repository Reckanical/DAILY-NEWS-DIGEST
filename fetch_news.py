import requests
from newspaper import Article

API_KEY = "5f44c9cc53434f79aa390a4794342b9e"

def get_full_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except:
        return ""

def fetch_news(query="", language="en", page_size=5):
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": API_KEY,
        "q": query,
        "language": language,
        "pageSize": page_size,
        "sortBy": "publishedAt"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("❌ Error fetching news:", response.status_code)
        return []

    articles = []
    for a in response.json().get("articles", []):
        full_text = get_full_article(a["url"])
        articles.append({
            "title": a["title"],
            "description": a["description"] or "",
            "url": a["url"],
            "source": a["source"]["name"],
            "content": full_text or a["description"]  # ✅ Use full text if available
        })
    return articles
