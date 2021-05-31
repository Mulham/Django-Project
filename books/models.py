from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=20)

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField('Category', related_name='books')
    image = models.FileField(upload_to="upload/")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    url = models.FileField(upload_to='books')
    author = models.CharField(max_length=60)

class Comment(models.Model):

    author = models.CharField(max_length=60)

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    book = models.ForeignKey('Book', on_delete=models.CASCADE)