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
        date_post = datetime.date.today()
        entries.append(
            {
                "entry_title": request.form.get("title"),
                "entry_content": request.form.get("content"),
                "date_post": date_post,
            }
        )

    print(entries)
    return render_template("home/home.html", title=title, year=current_year)


@app.get("/post")
def post():
    title = "posts"
    return render_template("home/recent.html", title=title, recent=entries)


if __name__ == "__main__":
    app.run(debug=True)
