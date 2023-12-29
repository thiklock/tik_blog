# blog/views.py

from django.shortcuts import render
from blog.models import Post, Comment
from django.http import HttpResponse
import subprocess

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/detail.html", context)


def streamlit_app(request):
    # Run the Streamlit app as a subprocess
    result = subprocess.run(["streamlit", "run", "path/to/streamlit_app.py"], capture_output=True, text=True)
    streamlit_output = result.stdout

    # Display the Streamlit output in a Django template
    return render(request, 'streamlit_app.html', {'streamlit_output': streamlit_output})
