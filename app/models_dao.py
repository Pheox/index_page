from app import db
from models import Bookmark, Tag, BookmarkTag


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
  def edit(id, name, url, note, tags):
    bm = Bookmark.query.get(id)
    bm.name = name
    bm.url = url
    bm.note = note
    bm.tags = tags
    db.session.commit()

  @staticmethod
  def delete(id):
    # TODO: delete also mappings
    bm = Bookmark.query.get(id)
    db.session.delete(bm)
    db.session.commit()

  @staticmethod
  def get_tag_bookmarks(tag_id):
    results = db.session.query(Bookmark, BookmarkTag, Tag).\
      join(BookmarkTag).join(Tag).\
      filter(BookmarkTag.tag_id == tag_id)

    results = [res[0] for res in results]
    return results

  @staticmethod
  def get_most_frequent():
    results = db.session.query(Bookmark).\
      order_by(Bookmark.usage_cnt.desc()).all()

    # results = [res[0] for res in results]
    results = results[:5]
    print results
    return results

  @staticmethod
  def inc_counter(bookmark_id):
    bookmark = Bookmark.query.get(bookmark_id)
    if bookmark:
      bookmark.usage_cnt = bookmark.usage_cnt + 1
      db.session.commit()

  @staticmethod
  def add_sample_data():
    bm1 = Bookmark(id=1, name="bm1", url="www.bm1.com")
    bm2 = Bookmark(id=2, name="bm2", url="www.bm2.com")
    bm3 = Bookmark(id=3, name="bm3", url="www.bm3.com")
    db.session.add(bm1)
    db.session.add(bm2)
    db.session.add(bm3)
    db.session.commit()

  @staticmethod
  def load_from_file(filename):
    bookmarks = []
    id_start = 100

    with open(filename,'r') as fh:
      content = fh.read()

    cnt = 0
    lines = content.split("\n")
    for line in lines:
      items = line.split(",")
      if len(items) < 2:
        continue
      cnt += 1
      bm = Bookmark(id=id_start+cnt, name=items[0].strip(), url=items[1].strip())
      db.session.add(bm)
    db.session.commit()

class TagDAO(object):

  @staticmethod
  def get_all():
    results = Tag.query.all()
    return results

  @staticmethod
  def add_sample_tags():
    tag1 = Tag(id=1, name="tag1")
    tag2 = Tag(id=2, name="tag2")
    db.session.add(tag1)
    db.session.add(tag2)
    db.session.commit()


class BookmarkTagDAO(object):

  @staticmethod
  def add_sample_bookmark_tags():
    bm_tag1 = BookmarkTag(bookmark_id=1, tag_id=1)
    bm_tag2 = BookmarkTag(bookmark_id=2, tag_id=2)
    bm_tag3 = BookmarkTag(bookmark_id=3, tag_id=2)

    db.session.add(bm_tag1)
    db.session.add(bm_tag2)
    db.session.add(bm_tag3)
    db.session.commit()

  @staticmethod
  def delete_bm(bookmark_id):
    results = BookmarkTag.query.filter(bookmark_id==bookmark_id).all()
    print results
    for result in results:
      print result
      db.session.delete(result)
    db.session.commit()

  @staticmethod
  def update_tags(bookmark_id, tags):
    tags = set([tag.strip() for tag in tags.split()])

    # TODO: create tags if needed
    BookmarkTagDAO.delete_bm(bookmark_id)

    for tag in tags:
      tag_obj = Tag.query.filter(Tag.name==tag).all()
      if not tag_obj:
        db.session.add(Tag(name=tag))
        db.session.commit()
      tag_id = Tag.query.filter(Tag.name==tag).all()[0].id
      print "adding " + str(bookmark_id) + str(tag_id)
      db.session.add(BookmarkTag(bookmark_id=bookmark_id, tag_id=tag_id))
      db.session.commit()
