from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from blog.models import Post


def frontpage(request):
    paginator = Paginator(Post.posts.all().select_related('category'), 12)
    page_number = request.GET.get('page', 1)

    try:
        posts_per_page = paginator.page(page_number)
    except EmptyPage:
        posts_per_page = paginator.page(1)

    context = {
        'posts': posts_per_page,
    }
    return render(request, 'core/frontpage.html', context)


def about(request):
    return render(request, 'core/about.html', {})


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
