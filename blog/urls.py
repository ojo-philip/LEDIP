from django.urls import path, include
from .views import (
    home_page,
    blog_page,
    post_detail,
    contact_page,
    about_page,
    # UsersPostListView,
    # tags_page,
    # post_create,
    # post_update,
    # post_delete,
    # load_more,
    # PostJsonListView
)


app_name = 'blog'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('blog/', blog_page, name='blog_page'),
    path('contact-us/', contact_page, name='contact_page'),
    path('about-us/', about_page, name='about_page'),
    # path('author/<str:username>', UsersPostListView.as_view(), name='users_post_list'),
    # path('load-more/', load_more, name='load_more'),
    # path('posts-json/<int:num_posts>/', PostJsonListView.as_view(), name='posts_json_view'),
    # path('tags/<int:pk>-<str:slug>/', tags_page, name='tags_page'),
    # path('categories/<int:pk>-<str:slug>/',
    #      category_page, name='category_page'),
    path('post/<int:pk>-<str:slug>/', post_detail, name='post_detail'),
    # path('post/<int:pk>-<str:slug>/edit/', post_update, name='post_update'),
    # path('post/<int:pk>-<str:slug>/delete/', post_delete, name='post_delete'),
    # path('search/', search, name='search'),
    # path('post-create/', post_create, name='post_create'),
]
