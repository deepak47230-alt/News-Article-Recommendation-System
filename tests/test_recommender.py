from recommender import NewsRecommender

def test_recommender_loads_articles():
    model = NewsRecommender("data/news.csv")
    assert len(model.articles) > 0

def test_recommend_returns_relevant_results():
    model = NewsRecommender("data/news.csv")
    results = model.recommend("artificial intelligence machine learning", top_n=3)
    assert results
    assert len(results) <= 3
    assert all("title" in item and "score" in item for item in results)

def test_blank_query_returns_empty_list():
    model = NewsRecommender("data/news.csv")
    assert model.recommend("   ") == []
