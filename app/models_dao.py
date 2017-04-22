from app import db
from models import Bookmark, Tag


class BookmarkDAO(object):

  @staticmethod
  def get_bm_url(bm_id):
    bm = Bookmark.query.get(bm_id)
    return bm.url

  @staticmethod
  def get_all():
    results = Bookmark.query.all()
    # for res in results:
    #   print res.name
    return results

  @staticmethod
  def add_sample_data():
    bm = Bookmark(id=1, name="demo_bm", url="www.google.com")
    db.session.add(bm)
    db.session.commit()


class TagDAO(object):

  @staticmethod
  def get_all():
    results = Tag.query.all()
    return results

  @staticmethod
  def add_sample_tags():
    tag1 = Tag(id=1, name="mavenir")
    db.session.add(tag1)
    db.session.commit()


class BookmarkTagDAO(object):

  @staticmethod
  def get_bookmarks(tag_id):
    results = Tag.query.all()
    return results

  @staticmethod
  def add_sample_bookmark_tags():
    tag1 = BookmarkTag(id=1, name="mavenir")
    db.session.add(tag1)
    db.session.commit()

