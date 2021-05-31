from flask import Flask, Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0")