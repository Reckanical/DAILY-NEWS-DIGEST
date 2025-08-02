import unittest
from fetch_news import fetch_news
from summarizer import summarize_text
from recommender import recommend_articles

class TestNewsAgent(unittest.TestCase):

    def test_fetch_news_returns_articles(self):
        articles = fetch_news(query="technology", page_size=2)
        self.assertIsInstance(articles, list)
        self.assertGreater(len(articles), 0)

        required_keys = {"title", "description", "url", "source", "content"}
        for key in required_keys:
            self.assertIn(key, articles[0])

    def test_summarize_text_creates_summary(self):
        text = "Artificial Intelligence is rapidly evolving and impacting many industries, including healthcare and finance."
        summary = summarize_text(text)
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 20) # Summary should be reasonably short
        self.assertNotEqual(summary.strip(), text.strip())  # Should be different

    def test_summarize_text_empty_string(self):
        summary = summarize_text("")
        self.assertEqual(summary, "No description available.")

    def test_recommend_articles_with_keywords(self):
        articles = [
            {"title": "Apple releases new iPhone", "description": "Apple launches new product", "url": "http://apple.com", "source": "TechNews", "content": ""},
            {"title": "Football match highlights", "description": "Local team wins", "url": "http://sports.com", "source": "SportsDaily", "content": ""}
        ]
        keywords = ["apple", "iphone"]
        filtered = recommend_articles(articles, keywords)
        self.assertEqual(len(filtered), 1) 
        self.assertIn("Apple", filtered[0]["title"])

    def test_recommend_articles_no_keywords_returns_all(self):
        articles = [
            {"title": "Some news", "description": "Some description", "url": "", "source": "News", "content": ""}
        ]
        filtered = recommend_articles(articles, [])
        self.assertEqual(filtered, articles)

if __name__ == "__main__":
    unittest.main()
