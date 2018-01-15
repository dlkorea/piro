from django.shortcuts import render
from django.utils import timezone


def blog_detail(request):
    content_title = '문서 제목입니다.!!!!'
    ctx = {
        'now': timezone.now(),
        'content_title': content_title,
        'range_10': range(10),
    }
    return render(request, 'core/blog_detail.html', ctx)


def first_dynamic(request, pk):
    ctx = {
        'pk': pk,
    }
    return render(request, 'core/first_dynamic.html', ctx)


def capture_string(request, url_path_str):
    ctx = {
        'path': url_path_str,
    }
    return render(request, 'core/first_dynamic.html', ctx)
