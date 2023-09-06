from django.contrib import admin
from .models import News, newsCategory

admin.site.register(News)
admin.site.register(newsCategory)

