from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    CategoryListCreateView,
    PostListCreateView,
    PostDetailView,
    CommentCreateView,
)

urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),

    # Categories
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),

    # Posts
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),

    # Comments
    path('posts/<slug:slug>/comments/', CommentCreateView.as_view(), name='comment-create'),
]