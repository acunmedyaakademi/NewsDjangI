
from django.contrib import admin
from .models import newsCategory, News

admin.site.register(News)
admin.site.register(newsCategory)

