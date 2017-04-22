from app import app

from flask import render_template

from models import Bookmark
from models_dao import BookmarkDAO, TagDAO


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/bookmarks')
def bookmarks():
  bookmarks = BookmarkDAO.get_all()
  tags = TagDAO.get_all()
  # print str(results)

  return render_template('index.html', bookmarks=bookmarks, tags=tags)
