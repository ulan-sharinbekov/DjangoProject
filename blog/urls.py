from django.urls import path
from django.contrib import admin
from .views import about,  contact, login,  BlogHome, BlogCategory, ShowPost, AddPage
#index, show_category, show_post, addpage,

urlpatterns = [

   # path('', index, name='home'),
    path('', BlogHome.as_view(), name='home'),
    path('about/', about, name='about'),
    #path('addpage/', addpage, name='add_page'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    #path('post/<slug:post_slug>/', show_post, name='post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    #path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    ]
