from django.shortcuts import render, get_object_or_404
from . models import newsCategory, News, Author


def homepage(request,):
    kategori = newsCategory.objects.all()
    haberler = News.objects.all()
    yazar = Author.objects.all()
    return render(request,"pages/homepage.html", {

        'kategori': kategori,
        'haberler': haberler,
        'yazar': yazar
    })

def news_detail(request, id, author_id):
    haber = get_object_or_404(News, id=id)
    yazar = Author.objects.get(Author, author_id=author_id)
    return render(request, 'pages/single-post.html', {
        'haber': haber,
        'yazar': yazar
    })

def category(request, category):
    kategori = get_object_or_404(News, category=category)
    return render(request, 'showbiz-category.html',{
        'kategori': kategori
    })










