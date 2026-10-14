from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class NewsRecommender:
    """Content-based news recommender using TF-IDF and cosine similarity."""
    def __init__(self, csv_path="data/news.csv"):
        path = Path(csv_path)
        if not path.exists():
            raise FileNotFoundError(f"Dataset not found: {path}. Run from the project root directory.")
        self.articles = pd.read_csv(path).fillna("")
        required = {"title", "category", "description", "url"}
        missing = required.difference(self.articles.columns)
        if missing:
            raise ValueError(f"Dataset is missing columns: {', '.join(sorted(missing))}")
        self.articles = self.articles.drop_duplicates(subset=["title"]).reset_index(drop=True)
        self.articles["content"] = (self.articles["title"].astype(str) + " " +
            self.articles["category"].astype(str) + " " + self.articles["description"].astype(str))
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(self.articles["content"])

    def recommend(self, interests, top_n=6):
        interests = str(interests).strip()
        if not interests or self.articles.empty:
            return []
        user_vector = self.vectorizer.transform([interests])
        scores = cosine_similarity(user_vector, self.matrix).flatten()
        ranked = scores.argsort()[::-1]
        results = []
        for idx in ranked:
            if scores[idx] <= 0:
                continue
            row = self.articles.iloc[idx]
            results.append({"title": str(row["title"]), "category": str(row["category"]),
                "description": str(row["description"]), "url": str(row["url"]),
                "score": round(float(scores[idx]), 3)})
            if len(results) >= max(1, int(top_n)):
                break
        return results
