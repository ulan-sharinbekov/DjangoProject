from django.urls import path
from django.contrib import admin
from .views import about,  contact,   BlogHome, BlogCategory, ShowPost, AddPage, RegisterUser, LoginUser, logout_user
#index, show_category, show_post, addpage,login,

urlpatterns = [

   # path('', index, name='home'),
    path('', BlogHome.as_view(), name='home'),
    path('about/', about, name='about'),
    #path('addpage/', addpage, name='add_page'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    #path('post/<slug:post_slug>/', show_post, name='post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    #path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    ]
