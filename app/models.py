from app import db
from datetime import datetime

"""
List of models:
- Bookmark
"""

class Bookmark(db.Model):
  __tablename__ = 'bookmark'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), index=True, nullable=False)
  url = db.Column(db.String(100), index=True, nullable=False)
  description = db.Column(db.String(100), index=True)

class Tag(db.Model):
  __tablename__ = 'tag'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), index=True, nullable=False)
  description = db.Column(db.String(100), index=True)


class BookmarkTag(db.Model):
  __tablename__ = 'bookmark_page'
  bookmark_id = db.Column(db.Integer, db.ForeignKey('bookmark.id'), primary_key=True)
  tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)
  bookmark = db.relationship('Bookmark', backref='bookmark_page')
