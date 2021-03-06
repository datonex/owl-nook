from django.db import models
from django.urls import reverse
from django.shortcuts import redirect
from owlnookuser.models import OwlNookUser
from cloudinary.models import CloudinaryField
from tinymce import models as tinymce_models


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    category_name = models.CharField(
        max_length=50,
        unique=True,
        default="uncategorised",
    )
    Description = models.TextField(blank=True)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        OwlNookUser, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = tinymce_models.HTMLField()
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.CharField(max_length=120, blank=False)
    likes = models.ManyToManyField(OwlNookUser, related_name="blog_likes", blank=True)
    dislikes = models.ManyToManyField(
        OwlNookUser, related_name="blog_dislikes", blank=True
    )
    bookmark = models.ManyToManyField(
        OwlNookUser, related_name="blog_bookmarks", blank=True
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        default="uncategorised",
        on_delete=models.SET_DEFAULT,
        related_name="blog_categories",
    )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["status", "-created_on"]

    def __unicode__(self):
        try:
            public_id = self.featured_image.public_id
        except AttributeError:
            public_id = ""
        return "Post <%s:%s>" % (self.title, public_id)

    def __str__(self):
        return self.title + " | " + str(self.author)

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()

    # https://realpython.com/django-redirects/
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.slug)])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.ForeignKey(
        OwlNookUser, on_delete=models.CASCADE, related_name="comments"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def number_of_comments(self):
        return self.post.count()


class Bookmark(models.Model):
    list_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="blog_posts")

    def __str__(self):
        return self.list_name
