from flask_wtf import FlaskForm
from wtforms import TextField, SelectField, FileField, HiddenField
from wtforms.validators import Required


class BookmarkEditForm(FlaskForm):
  bm_name = TextField('bm_name', validators=[Required()])
  bm_url = TextField('bm_url', validators=[Required()])
  bm_note = TextField('bm_note', validators=[])
  bm_tags = TextField('bm_tags', validators=[])
