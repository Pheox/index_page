from app import app

from flask import render_template

from models import Bookmark
from models_dao import BookmarkDAO, TagDAO, BookmarkTagDAO


@app.route('/')
def bookmarks(tag_id=None):
  bookmarks = BookmarkDAO.get_all()
  tags = TagDAO.get_all()
  # print str(results)

  if tag_id:
    bookmarks = BookmarkDAO.get_tag_bookmarks(tag_id)

  return render_template('index.html', bookmarks=bookmarks, tags=tags)


@app.route('/show/<int:tag_id>',
           methods=['GET', 'POST'])
def filter_by_tag(tag_id):
  return bookmarks(tag_id)
