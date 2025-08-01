import requests
import os

API_KEY = "5f44c9cc53434f79aa390a4794342b9e"

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

    articles = response.json().get("articles", [])
    return [
        {
            "title": a["title"],
            "description": a["description"] or "",
            "url": a["url"],
            "source": a["source"]["name"]
        }
        for a in articles
    ]
