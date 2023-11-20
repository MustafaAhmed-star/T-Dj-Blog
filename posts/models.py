from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=200)
    content  = models.TextField(max_length=2000)
    draft = models.BooleanField()
    publish_date = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    image = models.ImageField(default = 'static/images/1.png')
    def __str__(self):
        return f'{self.title} {self.id}'