from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

# dummy post data
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': "Augsut 27, 2018"
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': "Augsut 28, 2018"
    },
]


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',  context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

