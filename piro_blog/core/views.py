from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse

from .models import Article


def blog_detail(request, pk):
    article = Article.objects.get(pk=pk)
    ctx = {
        'article': article,
    }
    return render(request, 'core/blog_detail.html', ctx)


def blog_list(request):
    article_list = Article.objects.all()
    ctx = {
        'article_list': article_list,
    }
    return render(request, 'core/blog_list.html', ctx)


def blog_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article.objects.create(title=title, content=content)
        url = reverse('blog_detail', kwargs={'pk': article.pk, })
        return redirect(url)

    return render(request, 'core/blog_create.html')
