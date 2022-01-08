from django.urls import path
from django.conf.urls import url
from .views import PostList, PostDetail, AddPost, EditPost

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("articles/<slug:slug>", PostDetail.as_view(), name="post_detail"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("articles/edit/<slug:slug>", EditPost.as_view(), name="edit_post"),
    url(r"^add_post$", AddPost.as_view(), name="upload_post"),
    url(r"^articles/(?P<slug>[\w-]+)/$", EditPost.as_view(), name="reupload_post"),
]
