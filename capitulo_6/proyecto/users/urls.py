from users import views

from users.views import UserDetailView, SignUpView, UpdateProfileView, LoginView

from django.urls import path


urlpatterns = [
    # Managements
    path(
        route='login/',
        view=LoginView.as_view(),
        name='login'),
    path(
        route='logout/',
        view= views.logout_view,
        name='logout'),
    path(
        route='signup/',
        view=SignUpView.as_view(),
        name='signup'),
    path(
        route='me/profile/',
        view=UpdateProfileView.as_view(),
        name='update_profile'),

    #  Posts
    path(
        route='<str:username>/',
        view=UserDetailView.as_view(),
        name='detail',
    ),
]