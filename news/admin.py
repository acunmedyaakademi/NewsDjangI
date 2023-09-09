from django.contrib import admin
from .models import News, newsCategory, Author, Comments

admin.site.register(News)
admin.site.register(newsCategory)
admin.site.register(Author)
admin.site.register(Comments)