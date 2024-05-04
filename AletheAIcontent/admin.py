from django.contrib import admin
from .models import Post
from .models import Image

admin.site.register(Image)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)

