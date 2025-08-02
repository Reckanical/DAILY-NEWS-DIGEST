def recommend_articles(articles, keywords):
    if not keywords:
        return articles

    filtered = []
    for article in articles:
        content = (article.get("title", "") + " " + article.get("description", "")).lower()
        score = sum(1 for k in keywords if k.lower() in content)

        if score > 0:  
            article["score"] = score
            filtered.append(article)

    return filtered
