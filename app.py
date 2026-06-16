from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/learn-more")
def learn_more():
    return render_template("learn_more.html")


@app.route("/search")
def search():
    query = request.args.get("q", "").strip()

    # Replace this with your real data source (DB, API, etc.)
    sample_items = ["World Cup", "Match Highlights", "Team News", "Contact"]
    results = (
        [item for item in sample_items if query.lower() in item.lower()]
        if query
        else []
    )
    return render_template("search_results.html", query=query, results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
