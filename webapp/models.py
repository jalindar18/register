from django.db import models
from django.contrib.auth.admin import User


class Blog(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    subject = models.CharField(max_length=500)
    blog_text = models.TextField(default='Blog')
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


    def __str__(self):
        return self.title

