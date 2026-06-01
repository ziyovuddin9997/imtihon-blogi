from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    PostListCreateView,
    PostDetailView,
    CommentListCreateView,
    CommentDetailView,
    LikeToggle
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),

    path('comments/', CommentListCreateView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),

    path('like/', LikeToggle.as_view()),
]