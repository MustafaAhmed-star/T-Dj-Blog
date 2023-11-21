from django.contrib import admin
from .models import Post  ,Category



class PostAdmin(admin.ModelAdmin):
    list_display = ['title','category']
    list_filter = ['draft']
    search_fields  = ['title']
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
