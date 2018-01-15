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
