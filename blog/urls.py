from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("articles/<slug:slug>", views.PostDetail.as_view(), name="post_detail"),
    path("add_post/", views.AddPost.as_view(), name="add_post"),
    # URL for uploading post
    url(r"^add_post$", views.AddPost.as_view(), name="upload_post"),
]
