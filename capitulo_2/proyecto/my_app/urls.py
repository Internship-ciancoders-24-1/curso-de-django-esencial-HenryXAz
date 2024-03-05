from django.contrib import admin
from django.urls import path
from my_app import  views as local_views
from posts import views as post_views

urlpatterns = [     
    path('hello-world', local_views.hello_world),
    path('sorted', local_views.sort_numbers),
    path('hi/<str:name>/<int:age>', local_views.say_hi),
    path('posts', post_views.list_posts),
]

