from django.urls import path
from django.conf.urls import url
from .views import PostList, PostDetail, AddPost, EditPost, DeletePost

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("articles/<slug:slug>", PostDetail.as_view(), name="post_detail"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("articles/edit/<slug:slug>", EditPost.as_view(), name="edit_post"),
    path("articles/delete/<slug:slug>", DeletePost.as_view(), name="delete_post"),
    url(r"^add_post$", AddPost.as_view(), name="upload_post"),
    # https://stackoverflow.com/questions/19407239/generic-detail-view-must-be-called-with-either-an-object-pk-or-a-slug/19407315
    url(r"^articles/(?P<slug>[\w-]+)/$", EditPost.as_view(), name="reupload_post"),
    url(
        r"^articles/delete/(?P<slug>[\w-]+)/$", DeletePost.as_view(), name="remove_post"
    ),
]
