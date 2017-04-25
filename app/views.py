
from app import app

from flask import request, render_template, redirect, make_response
from models import Bookmark
from models_dao import BookmarkDAO, TagDAO, BookmarkTagDAO
from forms import BookmarkEditForm

import webbrowser


@app.route('/', methods=['GET', 'POST'])
def bookmarks(tag_id=None, bm_edit=None, edit_form=None):
  bookmarks = BookmarkDAO.get_all()
  tags = TagDAO.get_all()

  if tag_id:
    bookmarks = BookmarkDAO.get_tag_bookmarks(tag_id)

  most_frequent = BookmarkDAO.get_most_frequent()

  return render_template('index.html', bookmarks=bookmarks, tags=tags,
    bookmark_edit=bm_edit, edit_form=edit_form,
    bookmarks_frequent=most_frequent)


@app.route('/show/<int:tag_id>',
           methods=['GET', 'POST'])
def filter_by_tag(tag_id):
  return bookmarks(tag_id)


@app.route('/edit/<int:bookmark_id>',
           methods=['GET', 'POST'])
def bookmark_edit(bookmark_id):
  edit_form = BookmarkEditForm()

  if request.method == 'POST':
    form_submit_edit(bookmark_id, edit_form)

  return bookmarks(bm_edit=bookmark_id, edit_form=edit_form)


@app.route('/delete/<int:bookmark_id>', methods=['POST'])
def bookmark_delete(bookmark_id):
  BookmarkTagDAO.delete_bm(bookmark_id)
  BookmarkDAO.delete(bookmark_id)
  return redirect('/')


@app.route('/count/<int:bookmark_id>', methods=['GET', 'POST'])
def bookmark_count(bookmark_id):
  BookmarkDAO.inc_counter(bookmark_id)
  return redirect('/')


@app.route('/export', methods=['GET', 'POST'])
def export():
  bookmarks = BookmarkDAO.get_all()
  csv = ""
  for bm in bookmarks:
    bm_list = [bm.name, bm.url]
    csv += ",".join(bm_list)+"\n"

  response = make_response(csv)

  response.headers["Content-Disposition"] = "attachment; filename=bookmarks.csv"
  return response


# Helpers

def form_submit_edit(bookmark_id, form):
  BookmarkDAO.edit(bookmark_id, form.bm_name.data, form.bm_url.data,
    form.bm_note.data, form.bm_tags.data)
  BookmarkTagDAO.update_tags(bookmark_id, form.bm_tags.data)

  return True
