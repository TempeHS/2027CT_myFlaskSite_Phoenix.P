from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = "super_secret_key"


# -----------------------------
# Load language JSON files
# -----------------------------
def load_language(lang):
    path = os.path.join("languages", f"{lang}.json")
    if not os.path.exists(path):
        path = os.path.join("languages", "en.json")  # fallback
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# -----------------------------
# Translation function
# -----------------------------
def t(key):
    lang = session.get("language", "en")
    translations = load_language(lang)
    return translations.get(key, key)


# Make translation function available in templates
app.jinja_env.globals.update(t=t)


# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/world")
def world():
    return render_template("partials/world.html")


@app.route("/learn-more")
def learn_more():
    return render_template("learn_more.html")


@app.route("/new-skills")
def new_skills():
    return render_template("new_skills.html")


@app.route("/match-live")
def watch_live():
    return render_template("watch_live.html")


@app.route("/set_language/<lang>")
def set_language(lang):
    session["language"] = lang
    return redirect(request.referrer or url_for("home"))


@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()

    pages = [
        {"name": "Watch Live", "url": "/watch_live"},
        {"name": "New Skills", "url": "/new_skills"},
        {"name": "Contact", "url": "/contact"},
        {"name": "About", "url": "/about"},
        {"name": "World", "url": "/world"},
    ]

    results = [p for p in pages if query in p["name"].lower()]

    return render_template("search_results.html", query=query, results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
