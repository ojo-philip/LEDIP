from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
# from django.http import JsonResponse
# from django.core import serializers
# from django.template.loader import render_to_string
from django.db.models import Count
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db.models import Q
# from .forms import *
# from viewpage.models import *
# from viewpage.views import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
# from comment.forms import CommentForm
# from comment.models import Comment
from .pagination import pagination
# from urllib.parse import quote_plus
from django.views.generic import View
from django.views.generic import ListView
from team.models import Team

def home_page(request):
    featured = Post.objects.filter(featured=True, status='Published').order_by('-id')[:6]
    post = Post.objects.filter(status='Published').order_by('-updated')[:6]
    categories = Category.objects.all().order_by('id')
    teams = Team.objects.all()
    
    context = {
        'categories': categories,
        'featured': featured,
        'teams': teams,
    }
    return render(request, 'blog/index.html', context)

def about_page(request):
    teams = Team.objects.all()

    context = {
        'teams': teams,
    }
    return render(request, 'blog/about.html', context)


def contact_page(request):
    return render(request, 'blog/contact.html')


def blog_page(request):
    blog_posts = Post.objects.filter(status="Published")

    pages = pagination(request, blog_posts, 12)
    context = {
        # "blog_posts": blog_posts,
        'items': pages[0],
        'page_range': pages[1],
    }
    return render(request, "blog/article.html", context)


def post_detail(request, slug, pk):
    post_detail = get_object_or_404(Post, slug=slug, pk=pk)
    # share_shring = quote_plus(post_detail.content)
    recent_posts = Post.objects.filter(status="Published")[:3]
    context = {
        "post_detail": post_detail,
        "recent_posts": recent_posts,
        # "share_shring": share_shring,
    }
    return render(request, "blog/post.html", context)