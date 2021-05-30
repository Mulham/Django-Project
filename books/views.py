from django.shortcuts import redirect, render
from .models import Book, Comment
from .forms import BookForm, CommentForm
from django.contrib.auth.decorators import permission_required
# Create your views here.
def index(request):
    books = Book.objects.all().order_by('-created_on')

    context = {

        "books": books,

    }

    return render(request, "index.html", context)

@permission_required('auth.add_book')
def model_form_upload(request):

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            new_book = form.save()
            new_book.author = str(request.user)
            new_book.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

def book_detail(request, pk):

    book = Book.objects.get(pk=pk)
    form = CommentForm()

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = Comment(

                author=form.cleaned_data["author"],

                body=form.cleaned_data["body"],

                book=book

            )

            comment.save()

    comments = Comment.objects.filter(book=book)

    context = {

        "book": book,

        "comments": comments,

        "form": form,

    }


    return render(request, "book_detail.html", context)
