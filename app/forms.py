from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from wtforms import validators


class UploadForm(FlaskForm):
	description = TextAreaField('Description',[validators.DataRequired()])
	photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
