from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogEditView, BlogDeleteView, \
    BlogCinemaView, BlogMusicView, BlogMemView, BlogMakersView, BlogNewsView, ProfileView, EditProfileView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('cinema/', BlogCinemaView.as_view(), name='cinema'),
    path('music/', BlogMusicView.as_view(), name='music'),
    path('mem/', BlogMemView.as_view(), name='mem'),
    path('makers/', BlogMakersView.as_view(), name='makers'),
    path('news/', BlogNewsView.as_view(), name='news'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit/', EditProfileView.as_view(), name='edit_profile'),
]