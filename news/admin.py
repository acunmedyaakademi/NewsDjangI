from django.contrib import admin
from .models import News, newsCategory, Author

admin.site.register(News)
admin.site.register(newsCategory)
admin.site.register(Author)
