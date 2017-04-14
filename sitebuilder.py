#!/usr/bin/python3
import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
import datetime

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'toc']

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.template_filter('month')
def month(date: str) -> str:
    date = datetime.datetime.strptime(date, r"%d-%m-%Y")
    return date.strftime("%b")

@app.template_filter('day')
def day(date: str) -> str:
    date = datetime.datetime.strptime(date, r"%d-%m-%Y")
    return date.strftime("%d")

@app.template_filter('suffix')
def suffix(date: str) -> str:
    date = datetime.datetime.strptime(date, r"%d-%m-%Y")
    if 4 <= date.day <= 20 or 24 <= date.day <= 30:
        return "th"
    else:
        return ["st", "nd", "rd"][date.day % 10 - 1]

@app.route("/pygments.css")
def pygments_css() -> str:
    """
    return the pygments syntax-highlighting CSS
    """
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}

@app.route("/")
def index() -> str:
    """
    render the home page
    """
    return render_template('index.html', pages=pages)

@app.route('/page/<path:path>/')
def page(path: str) -> str:
    """
    render a page
    """
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/tag/<string:tag>/')
def tag(tag: str) -> str:
    """
    render a list of pages with a given tag
    """
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)
