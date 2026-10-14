# NewsMatch — News Article Recommendation System

A beginner-friendly news recommendation web app built with **Python, Flask, pandas, and scikit-learn**. Users enter interests (for example, “artificial intelligence” or “sports”) and receive related articles from the included demo dataset.

## Features
- Clean responsive web interface
- Content-based recommendations using TF-IDF and cosine similarity
- Included sample dataset so the project works without an external API key
- Model setup/check script and automated tests
- Health endpoint at `/health`

## Project structure
```text
news-article-recommendation-system/
├── app.py
├── recommender.py
├── build_models.py
├── requirements.txt
├── data/news.csv
├── templates/index.html
├── static/style.css
└── tests/test_recommender.py
```

## Run on Windows
1. Install Python 3.10 or newer.
2. Extract this folder and open Command Prompt inside it.
3. Create and activate a virtual environment:
   ```bat
   py -m venv .venv
   .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bat
   python -m pip install -r requirements.txt
   ```
5. Check the recommendation model:
   ```bat
   python build_models.py
   ```
6. Start the website:
   ```bat
   python app.py
   ```
7. Open **http://127.0.0.1:5000** in your browser.

## Run tests
```bat
python -m pytest
```

## How the recommendation works
1. The app combines each article's title, category, and description.
2. TF-IDF turns text into numerical vectors based on informative terms.
3. The user's topic is transformed into the same vector space.
4. Cosine similarity ranks articles by textual similarity.
5. The website shows the top matches.

The displayed percentage is a similarity score, not a calibrated probability.

## Dataset note
`data/news.csv` is a small, hand-written demo dataset for testing the app. Replace it with a properly licensed and maintained news dataset for a real deployment. Check the data provider's license and attribution requirements before publishing article text or images.

## Deployment
This is a local development project. Before deploying publicly, disable Flask debug mode, add production configuration, use a production WSGI server, validate external URLs, and review dataset/licensing requirements.

## Attribution
This is an independently assembled educational implementation. If you adapt another author's project or dataset, retain required attribution and comply with its license.
