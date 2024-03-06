from django.urls import path

from posts.views import PostListView, PostDetailView, CreatePostView

urlpatterns = [
    path(
        route='',
        view=PostListView.as_view(),
        name='feed'),

    path(
        route='posts/new/',
        view=CreatePostView.as_view(),
        name='create'),

    path(
        route='posts/<int:pk>/',
        view=PostDetailView.as_view(),
        name='detail',
    ),
]
