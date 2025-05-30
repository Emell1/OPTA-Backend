from django.contrib import admin

from blog import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "lang", "is_active", "created_at")
    search_fields = ("title", "description", "content")
    list_filter = ("lang", "is_active", "created_at")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "image")
    search_fields = ("name",)
    ordering = ("name",)
    date_hierarchy = "created_at"