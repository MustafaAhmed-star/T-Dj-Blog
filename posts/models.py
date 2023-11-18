from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content  = models.TextField(max_length=2000)
    draft = models.BooleanField()
    
    def __str__(self):
        return f'{self.title} {self.id}'