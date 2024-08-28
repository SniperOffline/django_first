from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='reg'),
    path('signUp', views.signUp, name='signUp'),
    path('signIn', views.signIn, name='signIn'),
    path('logIn', views.logIn, name='logIn'),
    path('logout', views.logout_url, name='logout'),
    path('create-blog-form', views.create_blog_form, name='create-blog-form'),
    path('create-blog', views.create_blog, name='create-blog'),
    path('blog/<int:blog_id>/', views.blog_model, name='blog-detail'),
    path('comment/<int:blog_id>/', views.add_comment, name='add-comment'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('delete_comment/<int:comment_id>/',views.delete_comment, name='delete_comment')
]