from flask import Flask
app = Flask(__name__)

#default route
@app.route("/")
def home():
    return "Hello World!"

@app.route("/about")
def about():
    return "Hello FinleySimula67!"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"
@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return f"{a} + {b} = {a+b}"

@app.route("/sub/<int:a>/<int:b>")
def sub(a,b):

    if a > b:
     return f"{a} - {b} = {a-b}"
    else:
     return f"{b} - {a}  = {b-a}"
if __name__ == "__main__":
   app.run(debug=False)