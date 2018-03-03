from flask import Flask
from flask import request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/life')
def life():
    return render_template('life.html')


@app.route('/code')
def code():
    return render_template('code.html')


@app.route('/experience')
def experience():
    return render_template('experience.html')



@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/1')
def hello():
    return render_template('hello.html')


@app.errorhandler(404)
def page_not_find(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
