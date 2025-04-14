from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('edit-post/<int:post_id>/', views.edit_post_view, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post_view, name='delete_post'),
    path('feed/', views.global_feed_view, name='global_feed'),
    path('post/<int:post_id>/', views.post_detail_view, name='post_detail'),


    


]
