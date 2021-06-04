from django.db import models

from django.core.exceptions import ValidationError
# Create your models here.
def validate_file_extension(value): 
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf','.doc','.docx']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!') 

class Category(models.Model):

    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField('Category', related_name='books')
    image = models.ImageField(upload_to="upload/")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='books', validators=[validate_file_extension])
    author = models.CharField(max_length=60)
    def __str__(self):
        return self.title
   
class Comment(models.Model):

    author = models.CharField(max_length=60)

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    