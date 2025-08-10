from flask import render_template, Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("matchimage.html")


if __name__ == "__main__":
    app.run(debug=True)