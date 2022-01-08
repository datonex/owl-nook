from django import forms
from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import Post
from .forms import PostForm


class PostList(generic.ListView):
    context_object_name = "posts"
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 2


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        posted = queryset.latest("created_on")
        comments = post.comments.order_by("created_on")
        liked = False
        disliked = False
        # if post.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        # if post.dislikes.filter(id=self.request.user.id).exists():
        #     disliked = True

        context = {
            "post": post,
            "posted": posted,
            # "comments": comments,
            # "commented": False,
            # "liked": liked,
            # "disliked": disliked,
        }
        return render(request, "post_detail.html", context)


class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

    def upload(request):
        context = dict(
            backend_form=PostForm(),
        )

        if request.method == "POST":
            # cloudinary backend upload
            form = PostForm(request.POST, request.FILES)
            context["posted"] = form.instance
            if form.is_valid():
                # Uploads image and creates a model instance for it
                form.save()

        return render(request, "post_detail.html", context)
