from django import forms
from .models import Post


# for cloudinary image upload -  https://cloudinary.com/documentation/django_image_and_video_upload
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "author",
            "title",
            "slug",
            "excerpt",
            "content",
            "category",
            "featured_image",
        ]

        widgets = {
            "author": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "excerpt": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }
