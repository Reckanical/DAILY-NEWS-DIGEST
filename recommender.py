def recommend_articles(articles, keywords):
    if not keywords:
        return articles

    filtered = []
    for article in articles:
        content = (article.get("title", "") + " " + article.get("description", "")).lower()
        if any(k.lower() in content for k in keywords):
            filtered.append(article)
    return filtered
