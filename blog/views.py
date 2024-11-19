from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

# This is the function-based view for the home page.
def index(request):
    message = "Welcome to our page!"
    return render(request, 'blog/hello.html', {'template_message': message})

# This is the class-based view for the list of posts in the blog.
class PostListView(ListView):
    model = Post

# This is the class-based view for the detail of a post in the blog.
class PostDetailView(DetailView):
    model = Post