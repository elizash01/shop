from django.urls import path, include
from rest_framework import routers

from .views import CategoryDetailViewSet, CategoryListViewSet, UserListView, UserDetailView, ClothesListViewSet

app_name = 'main'

router = routers.DefaultRouter()

router.register(r'categoty-list', CategoryListViewSet, basename='category-list')
router.register(r'category-detail', CategoryDetailViewSet, basename='category-detail')
router.register(r'clothes-list', ClothesListViewSet, basename='clothes-list')

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]