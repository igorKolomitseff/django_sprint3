from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post, Category


POST_LIST = Post.objects.select_related(
    'author', 'category', 'location'
).only(
    'id', 'title', 'text', 'pub_date', 'location',
    'author__username',
    'category__title', 'category__slug',
    'location__name', 'location__is_published'
).filter(
    pub_date__lte=timezone.now(),
    is_published=True,
)


def index(request):
    return render(request, 'blog/index.html', {
        'post_list': POST_LIST.filter(
            category__is_published=True
        )[:5],
    })


def post_detail(request, post_id):
    return render(request, 'blog/detail.html', {
        'post': get_object_or_404(
            POST_LIST.filter(
                category__is_published=True
            ),
            pk=post_id
        ),
    })


def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {
        'category': get_object_or_404(
            Category.objects.values(
                'title', 'description'
            ).filter(
                is_published=True
            ),
            slug=category_slug,
        ),
        'post_list': POST_LIST.filter(
            category__slug=category_slug,
        ),
    })
