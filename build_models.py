"""Check and report the content-based recommendation model setup."""
from recommender import NewsRecommender

def main():
    model = NewsRecommender("data/news.csv")
    print(f"Loaded {len(model.articles)} news articles.")
    print("TF-IDF vectors created successfully.")
    print("Model setup complete. Start the website with: python app.py")

if __name__ == "__main__":
    main()
