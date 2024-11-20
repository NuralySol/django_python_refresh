from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content','slug','image']
    success_url = reverse_lazy('post_list') # Redirects to the list of posts after creating a new post.
    template_name = 'blog/create.html' 

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content','slug','image']
    success_url = reverse_lazy('post_list') # Redirects to the list of posts after updating a post.
    template_name = 'blog/update.html'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')