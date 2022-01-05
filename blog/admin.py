from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = "content"
    list_display = ("author", "title", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on")
    summernote_fields = "content"
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category)
