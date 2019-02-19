from django.contrib import admin

from news.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['car', 'created_at', 'updated_at', 'description']
    fields = ['car', 'description']

    readonly_fields = ["created_at", "updated_at"]
