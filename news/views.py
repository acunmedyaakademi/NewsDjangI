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
def news_detail(request, slug):
    haber = get_object_or_404(News, slug=slug)
    yorumlar = haber.yorumlar.order_by('-id')
    if request.method == 'POST':
        form = CommentsForms(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = haber
            comment.save()
            messages.success(request, 'Yorum başarıyla eklendi')
            return redirect('news_detail', haber.slug)
    else:
        form = CommentsForms()

    return render(request, 'pages/single-post.html', {
        'haber': haber,
        'yazar': haber.author,
        'form': form,
        'yorumlar': yorumlar,
    })

def category_detail(request, category_slug ):
    category = get_object_or_404(newsCategory, slug=category_slug)
    categories = newsCategory.objects.all()
    news_in_category = News.objects.filter(category=category).order_by('-created_on')
    return render(request, 'pages/showbiz-category.html',{
        'category': category,
        'categories': categories,
        'news_in_category': news_in_category
    })



def contact(request):
    return render(request, 'pages/contact.html')












