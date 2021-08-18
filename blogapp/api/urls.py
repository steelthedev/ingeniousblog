
from django.urls import path
from . import views 
from accounts.views import *



urlpatterns = [
    path('blog', views.BlogView , name ='blog'),
    path('blog/view-post/<slug:slug>', views.ViewPost , name="view_post"),
    path('blog/delete/<slug:slug>', views.DeleteBlog , name = "delete-post"),
    path('blog/update/<slug:slug>',views.UpdateBlog, name="update-post"),
    path('accounts/create', RegisterUser , name="register")
    
]