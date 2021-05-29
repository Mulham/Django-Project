from django.contrib import admin
from .models import Book, Category

# Register your models here.

class BookAdmin(admin.ModelAdmin):

    pass


class CategoryAdmin(admin.ModelAdmin):

    pass

admin.site.register(Book, BookAdmin)

admin.site.register(Category, CategoryAdmin)