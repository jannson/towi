from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Author

admin.site.register(Author, PageAdmin)
print 'aaaa'
