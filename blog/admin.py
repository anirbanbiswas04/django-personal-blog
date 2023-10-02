from django.contrib import admin
from .models import Category, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title']
    list_display = ['title', 'slug']


class CommentItemInline(admin.TabularInline):
    model = Comment
    extra = 0
    raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'intro']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']
    list_filter = ['post', 'created_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
