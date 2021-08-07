from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name = 'index'),
    path('post/<str:pk>', views.post, name = 'post'),
    path('profile/<str:uid>', views.profile, name = 'profile'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = "logout"),
    path('add_post', views.add_post, name = "add_post")
]