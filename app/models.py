from app import db
from datetime import datetime

"""
List of models:
- Bookmark
- Tag
- BookmarkTag
"""


class Bookmark(db.Model):
  __tablename__ = 'bookmark'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), index=True, nullable=False)
  url = db.Column(db.String(100), index=True, nullable=False)
  note = db.Column(db.String(100), default="")
  tags = db.Column(db.String(100), default="")
  usage_cnt = db.Column(db.Integer, default=0)


class Tag(db.Model):
  __tablename__ = 'tag'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), index=True, nullable=False)
  note = db.Column(db.String(100), default="")


class BookmarkTag(db.Model):
  __tablename__ = 'bookmark_tag'
  bookmark_id = db.Column(db.Integer, db.ForeignKey('bookmark.id'),
    primary_key=True)
  tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'),
    primary_key=True)
