from django.shortcuts import redirect, render
from .models import Comment, Post
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
    comments = Comment.objects.filter(post=post)
    context = {
    'post':post,
    'comments':comments,
    
    }
    return render(request,'posts/post_detail.html',context)
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        
        if form.is_valid():
          myform =  form.save(commit = False)
          myform.author = request.user
          myform.save()
          return redirect('/posts/')
    form = PostForm()
    return render(request,'posts/post_form.html',{'form':form})
def post_edit(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance = post)
        
        if form.is_valid():
          myform =  form.save(commit = False)
          myform.author = request.user
          myform.save()
          return redirect('/posts/')
    form = PostForm(instance = post)
    return render(request,'posts/post_edit.html',{'form':form})    
def post_delete(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/posts/')
    
    
    
class PostList(generic.ListView):
    model = Post    
class PostDetail(generic.DetailView):
    model = Post

class PostCreate(generic.CreateView):
    model = Post
    form_class = PostForm
    success_url = '/posts/'
    
class PostDelete(generic.DeleteView):
    model = Post
    success_url = '/'