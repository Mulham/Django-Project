
from .forms import CustomUserCreationForm, EditProfileForm
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect, render

from django.urls import reverse
# Create your views here.
def dashboard(request):

    return render(request, "users/dashboard.html")

def register(request):

    if request.method == "GET":

        return render(

            request, "users/register.html",

            {"form": CustomUserCreationForm}

        )

    elif request.method == "POST":

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect(reverse("blog_index"))

def edit_profile(request):
    if request.method == "GET":

        return render(

            request, "users/edit_profile.html",

            {"form": EditProfileForm(instance=request.user)}

        )
    
    elif request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse("edit_profile"))
        else:
            form = EditProfileForm(instance=request.user)
            args = {'form': form}
            return render(reverse("edit_profile"))