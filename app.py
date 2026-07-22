from flask import Flask, render_template, request

app = Flask(__name__)


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

    results = []

    if query:
        for page in pages:
            if query in page["name"].lower():
                results.append(page)

    return render_template("search_results.html", query=query, results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
