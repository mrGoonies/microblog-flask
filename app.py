from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
entries = list()


@app.post("/")
@app.get("/")
def home():
    current_year = datetime.date.today().year
    title = "Home"

    if request.method == "POST":
        entry_title = request.form.get("title")
        date_post = datetime.date.today().strftime("%Y-%m-%d")
        entry_content = request.form.get("content")
        entries.append((entry_title, date_post, entry_content))
    print(entries)

    return render_template("home/home.html", title=title, year=current_year)


@app.get("/post")
def post():
    title = "posts"
    return render_template("home/recent.html", title=title, entries=entries)


if __name__ == "__main__":
    app.run(debug=True)
