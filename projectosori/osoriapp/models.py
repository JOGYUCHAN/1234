from django.db import models
from django.forms import CharField, DateTimeField

# 게시물 모델

class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment