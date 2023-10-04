from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.get("/home")
@app.get("/")
def home():
    current_year = datetime.date.today().year
    title = "Home"
    return render_template("base.html", title=title, year=current_year)


if __name__ == "__main__":
    app.run()
