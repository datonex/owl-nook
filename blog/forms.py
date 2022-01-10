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
            "featured_image",
            "content",
            "category",
        ]

        widgets = {
            "author": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "excerpt": forms.TextInput(attrs={"class": "form-control"}),
            "featured_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "excerpt",
            "featured_image",
            "content",
            "category",
        ]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "excerpt": forms.TextInput(attrs={"class": "form-control"}),
            "featured_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }
