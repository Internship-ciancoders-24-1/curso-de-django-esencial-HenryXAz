from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from my_app import views as local_views

urlpatterns = [    
    path('admin', admin.site.urls), 
    path('hello-world/', local_views.hello_world, name='hello_world'),
    path('sorted/', local_views.sort_numbers, name='sort'),
    path('hi/<str:name>/<int:age>/', local_views.say_hi, name='hi'),

    path('', include(('posts.urls', 'posts'), namespace='posts')),

    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

