from flask import Flask, render_template

app = Flask(__name__)

@app.route("/template")
def templateCall():
    return render_template("index.html", name="Nabin")

@app.route("/page")
def page():
    return render_template("page.html", name="Nabin")
if __name__ == "__main__":
   app.run(debug=False)