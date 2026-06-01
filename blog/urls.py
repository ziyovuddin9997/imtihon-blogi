from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    ProfileView,
    PostListCreateView,
    PostDetailView,
    CommentListCreateView,
    CommentDetailView,
    LikeCreateView,
    LikeDeleteView
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', ProfileView.as_view()),

    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),

    path('comments/', CommentListCreateView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),

    path('like/', LikeCreateView.as_view()),
    path('unlike/', LikeDeleteView.as_view()),
]