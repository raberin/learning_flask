from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    # name = request.args.get("name", "World")
    return f'<h1>Home Page</h1>'


@app.route('/about')
def about():
    # name = request.args.get("name", "World")
    return f'<h1>About Page</h1>'


if __name__ == '__main__':
    app.run(debug=True)
