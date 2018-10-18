from django.urls import path

from MyBlog import views

urlpatterns = [
    path('blog/', views.get_blog, name='Blog'),
    path('<int:blog_id>/detail/', views.get_details, name='blog_get_detail'),
]
