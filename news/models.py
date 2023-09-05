from django.db import models
from autoslug import AutoSlugField


class newsCategory(models.Model):
     name = models.CharField(max_length=120)
     class Meta:
         db_table = 'NewsCategories'
         verbose_name = 'Haber Kategorisi'
         verbose_name_plural = 'Haber Kategorileri'

     def __str__(self):
         return self.name


class News(models.Model):
    title = models.CharField(max_length=120)
    summary = models.TextField(max_length=300)
    contents = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(newsCategory, on_delete=models.CASCADE, related_name='news')
    slug = AutoSlugField(populate_from='baslik', unique=True, editable=True, blank=True)

    class Meta:
        db_table = 'News'
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


