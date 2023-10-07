from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import datetime
import os

app = Flask(__name__)

load_dotenv()
user = os.environ.get("MONGO_USER")
pwd = os.environ.get("MONGO_PWD")
client = MongoClient(f"mongodb+srv://{user}:{pwd}@cluster0.4pqdtun.mongodb.net/")
app.db = client.MicroBlog


@app.post("/")
@app.get("/")
def home():
    current_year = datetime.date.today().year
    title = "Home"

    if request.method == "POST":
        # Obteniendo valores del formulario
        entry_title = request.form.get("title")
        date_post = datetime.date.today().strftime("%Y-%m-%d")
        entry_content = request.form.get("content")

        # Agregando datos a MongoDB
        app.db.entries.insert_one(
            {"title": entry_title, "date": date_post, "content": entry_content}
        )

    return render_template("home/home.html", title=title, year=current_year)


@app.get("/post")
def post():
    title = "posts"
    posts = [obj for obj in app.db.entries.find()]

    return render_template("home/recent.html", title=title, entries=posts)


if __name__ == "__main__":
    app.run(debug=True)
