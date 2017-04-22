from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path

db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

# initialize database
from app.models_dao import BookmarkDAO, TagDAO, BookmarkTagDAO

BookmarkDAO.add_sample_data()
BookmarkDAO.load_from_file("data/bookmarks.txt")
TagDAO.add_sample_tags()
BookmarkTagDAO.add_sample_bookmark_tags()
