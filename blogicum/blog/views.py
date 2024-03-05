from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post, Category


def post_filter(post_object=Post.objects):
    return post_object.select_related(
        'author', 'category', 'location'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    return render(request, 'blog/index.html', {
        'post_list': post_filter()[:5],
    })


def post_detail(request, post_id):
    return render(request, 'blog/detail.html', {
        'post': get_object_or_404(
            post_filter(),
            pk=post_id
        ),
    })


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects,
        slug=category_slug,
        is_published=True
    )
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_filter(category.posts),
    })
