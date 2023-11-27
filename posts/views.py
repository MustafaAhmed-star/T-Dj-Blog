from django.shortcuts import render
from .models import Post
from django.views import generic
from .forms import PostForm
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
    'posts':posts,
             }
    return render(request,'posts/post_list.html',context)   
def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    context = {
    'post':post,
    
    }
    return render(request,'posts/post_detail.html',context)
# def post_create(request):
#     form = PostForm()
#     return render(request,'posts/post_create.html',{'form':form})
class PostList(generic.ListView):
    model = Post    
class PostDetail(generic.DetailView):
    model = Post