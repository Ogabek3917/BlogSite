from django.urls import path
from .views import  index,   addpost, detail,search_post,edit_post , logoutUser, delete_post,loginUser

urlpatterns = [
    path('',index,name="index"),
    path('addpost/', addpost, name="addpost"),
    path('detail/<int:post_id>/', detail, name="detail"),
    path('search/', search_post, name="search"),
    path('editpost/<int:post_id>/', edit_post, name="editpost"),
    path('logout/', logoutUser, name="logout"),
    path('deletepost/<int:post_id>/', delete_post, name="deletepost"),
    path('login/', loginUser, name="login"),
    path('post/<int:post_id>/', detail, name="detail"),
    
]