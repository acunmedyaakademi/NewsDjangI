from django.shortcuts import render, get_object_or_404
from . models import newsCategory, News


def homepage(request,):
    kategori = newsCategory.objects.all()
    haberler = News.objects.all()
    return render(request,"pages/homepage.html", {

        'kategori': kategori,
        'haberler': haberler
    })

def news_detail(request, id):
    haber = get_object_or_404(News, id=id)
    return render(request, 'pages/single-post.html', {
        'haber': haber
    })







