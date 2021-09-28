from django.contrib import admin
from django.urls import path , include
from blog import views

urlpatterns = [
    path('', views.index , name="home"),
    path('search', views.search , name="search"),
    path('addblog', views.addblog , name="addblog"),
    path('addnews', views.addnews , name="addnews"),
    path('deletecmt/<int:cmtid>', views.deletecmt , name="deletecmt"),
    path('dev', views.dashboard , name="dev"),
    path('login', views.loginpage , name="login"),
    path('logout', views.logoutpage , name="logout"),
    path('blogpage/<int:myid>', views.blogpage , name="blog"),
    # path('like/<int:myid>/<int:cid>/<int:no>', views.likeadd , name="like"),
]