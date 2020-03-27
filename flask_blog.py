from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'March 27, 2020'
    },
    {
        'author': 'Roenz Aberin',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'March 28, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    # name = request.args.get("name", "World")
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
