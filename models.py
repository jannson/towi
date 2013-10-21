from django.db import models
from mezzanine.blog.models import BlogPost
from mezzanine.pages.models import Page

class Author(Page):
    dob = models.DateField("Date of birth")

class Book(Page):
    author = models.ForeignKey("Author")
    cover = models.ImageField(upload_to="authors")
