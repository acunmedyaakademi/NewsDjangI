from django.shortcuts import render, get_object_or_404
from . models import newsCategory, News, Author


def homepage(request,):
    kategori = newsCategory.objects.all()
    haberler = News.objects.all()
    yazarlar = Author.objects.all()
    return render(request,"pages/homepage.html", {

        'kategori': kategori,
        'haberler': haberler,
        'yazarlar': yazarlar
    })

def news_detail(request, id):
    haber = get_object_or_404(News, id=id)
    return render(request, 'pages/single-post.html', {
        'haber': haber,
        'yazar': haber.author
    })

def category(request, category):
    kategori = get_object_or_404(News, category=category)
    return render(request, 'showbiz-category.html',{
        'kategori': kategori
    })










