# blog/urls.py

from django.urls import path
from . import views
from .views import streamlit_app
from .views import github_profile


urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('streamlit/', streamlit_app, name='streamlit_app'),
    path('thiklock/', github_profile, name='github_profile'),
    
]
