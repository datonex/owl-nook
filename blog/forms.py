from django import forms
from .models import Post
from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField

# Next two lines are only used for generating the upload preset sample name
from cloudinary.compat import to_bytes
import cloudinary, hashlib


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


class PhotoDirectForm(PostForm):
    featured_image = CloudinaryJsFileField(attrs={"class": "form-control"})


class PhotoUnsignedDirectForm(PostForm):
    upload_preset_name = (
        "sample_"
        + hashlib.sha1(
            to_bytes(cloudinary.config().api_key + cloudinary.config().api_secret)
        ).hexdigest()[0:10]
    )
    featured_image = CloudinaryUnsignedJsFileField(upload_preset_name)
