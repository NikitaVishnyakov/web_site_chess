from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/about/<string:name>/<int:id>')
def user_page(name, id):
    return "User page " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True)
