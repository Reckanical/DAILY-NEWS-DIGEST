# DAILY-NEWS-DIGEST

This project fetches news articles based on user input, summarizes them using an AI model, and filters them according to provided keywords.

Overview of How It Works:

- fetch_news.py

Uses NewsAPI to retrieve news articles related to a query.
Also uses newspaper3k to extract the full article text from each article URL.
Returns a list of articles with title, description, source, URL, and full content.

- summarizer.py
Uses HuggingFace Transformers (BART model) to summarize the article content.
If full article is too long, it truncates it.
Returns a short paragraph summary.

- recommender.py

Filters the articles by checking whether any of the user keywords appear in the title or description.
Returns the filtered list.

- app.py (or main.py)

Streamlit-based user interface.
Asks for number of articles and keywords.
Fetches articles, summarizes them, filters them, and displays results.
Saves results to a JSON file.

Requirements:
Install required libraries:

pip install -r requirements.txt

How to Run

streamlit run app.py
