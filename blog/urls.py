from django.urls import path
from . import views

urlpatterns = [
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/list/', views.PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView().as_view(), name='post-delete'),

]
