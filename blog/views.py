# blog/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.http import HttpResponse
import subprocess
from django.shortcuts import render
import streamlit as st
from io import StringIO
import sys

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
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog/detail.html", context)


def streamlit_app(request):
    # Redirect Streamlit's stdout to a StringIO object
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        # Run the Streamlit app in API mode
        with st.echo():
            streamlit.api._main_run(file_path="/home/chic-acer-ubu/repos/django_blog/streamlit_app_demo.py", args=["run", "--server.headless=true"])
        streamlit_output = sys.stdout.getvalue()
    except Exception as e:
        streamlit_output = f"Error running Streamlit app: {str(e)}"
        print(e)
    finally:
        # Reset Streamlit's stdout to the original value
        sys.stdout = old_stdout

    # Return the Streamlit output as plain text with content type 'text/plain'
    return HttpResponse(streamlit_output, content_type='text/plain')

import requests
from django.shortcuts import render

def github_profile(request):
    # Replace 'YOUR_GITHUB_USERNAME' with your actual GitHub username
    github_username = 'YOUR_GITHUB_USERNAME'
    github_profile_url = f'https://api.github.com/users/{github_username}'
    
    response = requests.get(github_profile_url)
    github_profile_data = response.json()

    return render(request, 'github_profile.html', {'github_profile_data': github_profile_data})