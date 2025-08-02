import streamlit as st
import json
from fetch_news import fetch_news
from summarizer import summarize_text
from recommender import recommend_articles
from datetime import datetime
import os

LIKED_FILE = "liked_articles.json"

def save_liked_article(article):
    liked = []
    if os.path.exists(LIKED_FILE):
        with open(LIKED_FILE, "r", encoding="utf-8") as f:
            liked = json.load(f)
    liked.append(article)
    with open(LIKED_FILE, "w", encoding="utf-8") as f:
        json.dump(liked, f, indent=2, ensure_ascii=False)

st.set_page_config(page_title="News Recommender", layout="centered")
st.title("📰 Daily News Recommender")

query = st.text_input("Enter keywords (comma-separated):", "technology, AI")
language = st.selectbox("Language:", ["en", "ar"])
page_size = st.slider("Number of articles:", 1, 10, 5)

if st.button("🔍 Fetch News"):
    keywords = [k.strip().lower() for k in query.split(",") if k.strip()]
    search_query = " OR ".join(keywords)

    with st.spinner("Fetching news..."):
        articles = fetch_news(query=search_query, language=language, page_size=page_size)

    if not articles:
        st.error("⚠️ No articles found.")
    else:
        for article in articles:
            article["summary"] = summarize_text(article.get("content", article["description"]))

        filtered_articles = recommend_articles(articles, keywords)

        if not filtered_articles:
            st.warning("🚫 No articles matched your keywords.")
        else:
            st.success(f"✅ Found {len(filtered_articles)} articles")

            for article in filtered_articles:
                st.subheader(article["title"])
                st.caption(f"Source: {article['source']}")
                st.write(article["summary"])
                st.markdown(f"[Read More]({article['url']})")

                if st.button(f"👍 Like this", key=article["url"]):
                    save_liked_article(article)
                    st.toast("✅ Saved to liked articles!")

            filename = f"newsresults_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(filtered_articles, f, indent=2, ensure_ascii=False)

            st.download_button(
                label="📥 Download Results",
                data=json.dumps(filtered_articles, indent=2, ensure_ascii=False),
                file_name=filename,
                mime="application/json"
            )
