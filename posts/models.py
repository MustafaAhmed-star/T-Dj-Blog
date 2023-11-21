from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content  = models.TextField(max_length=2000)# I can add TextField without max_length
    draft = models.BooleanField()
    publish_date = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    image = models.ImageField(default ='1.png')
    
    
    def __str__(self):
        return f'{self.title} {self.id}'