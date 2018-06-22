from django.urls import path
from .views import get_index, edit_post, new_post, post_detail

urlpatterns = [
    path('new/', new_post, name='new_post'),
    path('<int:pk>/edit', edit_post, name='edit_post'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('', get_index, name='get_posts'),
    ]