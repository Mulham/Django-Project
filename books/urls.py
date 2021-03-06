from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.book_detail, name="book_detail"),
    path("create/", views.model_form_upload, name="create"),
    path("<int:pk>", views.github, name="github"),
    path("category/<category>/", views.book_category, name="book_category"),
]