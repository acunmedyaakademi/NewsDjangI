from django.db import models
from autoslug import AutoSlugField



class Author(models.Model):
    name = models.CharField(max_length=120)
    about = models.TextField()
    image = models.ImageField(upload_to='news_author_images/', default='default_image.jpg')


    class Meta:
        db_table = 'Author'
        verbose_name = 'Yazar'
        verbose_name_plural = 'Yazar'


    def __str__(self):
        return self.name


class newsCategory(models.Model):
     name = models.CharField(max_length=120)
     slug = AutoSlugField(populate_from='isim', unique=True, editable=True, blank=True)

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
    category = models.ForeignKey(newsCategory, on_delete=models.CASCADE, related_name='kategori')
    slug = AutoSlugField(populate_from='baslik', unique=True, editable=True, blank=True)
    image = models.ImageField(upload_to='news_images/', default='default_image.jpg')
    author = models.ForeignKey(Author,on_delete=models.CASCADE, blank=False, default="Yazar")


    class Meta:
        db_table = 'News'
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title






class Comments(models.Model):
    name_surname = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    comment = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="yorumlar")

    class Meta:
        db_table = 'Comments'
        verbose_name = 'Yorumlar'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return self.name_surname



