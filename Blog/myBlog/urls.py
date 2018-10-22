from django.urls import path

from myBlog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('regist/', views.regist, name='regist'),
    path('blog/', views.get_blog, name='get_blog'),
    path('<int:blog_id>/detail/', views.blog_detail, name='blog_detail')
]
