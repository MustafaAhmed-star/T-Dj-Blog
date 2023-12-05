from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def postListApi(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def postDetailApi(request,pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)