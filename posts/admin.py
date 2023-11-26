from django.contrib import admin
from .models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ['title']
    list_filter = ['draft']
    search_fields  = ['title']
    summernote_fields = ['content']
admin.site.register(Post ,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
