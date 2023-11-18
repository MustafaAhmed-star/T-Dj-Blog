from django.contrib import admin
from .models import Post  



class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['draft']
    search_fields  = ['title']
admin.site.register(Post,PostAdmin)
