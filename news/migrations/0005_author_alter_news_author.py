# Generated by Django 4.2.5 on 2023-09-07 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('about', models.TextField()),
                ('image', models.ImageField(default='default_image.jpg', upload_to='news_author_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(default='Yazar', on_delete=django.db.models.deletion.CASCADE, to='news.author'),
        ),
    ]