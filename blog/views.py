from django.db.models import Q, Prefetch
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage
from .models import Category, Post
from .forms import CommentForm


def detail(request, category_slug, slug):
    post = get_object_or_404(Post.posts.prefetch_related('comments').select_related('category'), slug=slug)
    related = Post.posts.filter(category__slug=category_slug).exclude(id=post.id)[:5]

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'related': related,
        'form': form
    }
    return render(request, 'blog/detail.html', context)


def category(request, slug):
    category = get_object_or_404(Category.objects.prefetch_related(Prefetch('posts', queryset=Post.posts.all())),
                                 slug=slug)
    paginator = Paginator(category.posts.all(), 12)
    page_number = request.GET.get('page', 1)

    try:
        posts_per_page = paginator.page(page_number)
    except EmptyPage:
        posts_per_page = paginator.page(1)

    return render(request, 'blog/category.html', {'category': category, 'posts': posts_per_page, })


def search(request):
    query = request.GET.get('query', '')
    if query == '':
        posts = ''
    else:
        posts = Post.posts.filter(
            Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query)).select_related('category')

    paginator = Paginator(posts, 12)
    page_number = request.GET.get('page', 1)

    try:
        posts_per_page = paginator.page(page_number)
    except EmptyPage:
        posts_per_page = paginator.page(1)

    return render(request, 'blog/search.html', {'posts': posts_per_page, 'query': query})
