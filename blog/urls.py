from django.urls import path

from blog.views import main

app_name="blog"
urlpatterns=[
    path('',main)
]