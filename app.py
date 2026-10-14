from flask import Flask, render_template, request
from recommender import NewsRecommender

app = Flask(__name__)
recommender = NewsRecommender("data/news.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    recommendations = []
    message = None
    if request.method == "POST":
        query = request.form.get("interests", "").strip()
        if query:
            recommendations = recommender.recommend(query, top_n=6)
            if not recommendations:
                message = "No matching articles were found. Try different keywords."
        else:
            message = "Please enter a topic or your interests."
    return render_template("index.html", query=query, recommendations=recommendations, message=message)

@app.route("/health")
def health():
    return {"status": "ok", "articles_loaded": len(recommender.articles)}

if __name__ == "__main__":
    app.run(debug=True)
