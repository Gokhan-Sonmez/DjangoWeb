from django.contrib import admin

from article.models import *


class PostImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_at', 'status']
    list_filter = ['status']
    list_editable = ["status"]


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'create_at', 'image_tag', 'status']
    list_display_links = ["title", "create_at"]
    list_filter = ['status', 'category']
    list_editable = ["status", 'category']
    search_fields = ["title"]
    inlines = [PostImageInline]
    readonly_fields = ('image_tag',)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Images, ImagesAdmin)


admin.site.register(Category, CategoryAdmin)


admin.site.register(Post, PostAdmin)