from flask import Flask, jsonify
import feedparser

app = Flask(__name__)

RSS_FEED_URL = "http://www.livreshebdo.fr/rss.xml"  # Assurez-vous que l'URL est correcte

@app.route('/')
def home():
    # Parse le flux RSS
    feed = feedparser.parse(RSS_FEED_URL)
    # Extrayez les entrées du flux
    entries = feed.entries
    # Préparez une liste pour stocker les données formatées
    articles = []

    for entry in entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'description': entry.get('description', ''),
            'published': entry.get('published', '')
        })

    # Utilisez jsonify pour renvoyer les articles en JSON
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)