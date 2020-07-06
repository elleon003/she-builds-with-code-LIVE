from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=all_posts)

all_posts = [
    {
        'title': 'Post 1',
        'subtitle': 'This is the content of post 1.'
    },
    {
        'title': 'Post 2',
        'subtitle': 'This is the content of post 2.'
    },
    {
        'title': 'Post 3',
        'subtitle': 'This is the content of post 3.'
    },
]


if __name__ == '__main__':
    app.run()