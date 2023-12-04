from django import serializers
from .models import Post







class PostSerializer(serializers.ModelSerializers):
    class Meta:
        model  = Post
        exclude = ['publish_date','author',]

