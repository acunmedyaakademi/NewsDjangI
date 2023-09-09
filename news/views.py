from django.shortcuts import render, get_object_or_404, redirect
from .models import newsCategory, News, Author, Comments
from .forms import CommentsForms
from django.contrib import messages


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
    yorumlar = haber.comments.order_by('-id')
    if request.method == 'POST':
        form = CommentsForms(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.haber = haber
            comment.save()
            messages.success(request, 'Yorum başarıyla eklendi')
            return redirect('news_detail', haber.id)
    else:
        form = CommentsForms()

    return render(request, 'pages/single-post.html', {
        'haber': haber,
        'yazar': haber.author,
        'yorumlar': yorumlar,
        'form': form
    })

def category(request, category):
    kategori = get_object_or_404(News, category=category)
    return render(request, 'showbiz-category.html',{
        'kategori': kategori
    })










