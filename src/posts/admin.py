from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']
    list_display_links = ['updated']
    list_filter = ['timestamp','updated']
    readonly_fields = ['timestamp','updated']
    search_fields =['title','content']
    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
