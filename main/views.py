from rest_framework import viewsets, mixins, generics, permissions
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Clothes, Category, Brand, ClothesSize, ClothesColor, ClothesInStock
from .serializers import CategoryListSerializer, CategoryDetailSerializer, UserSerializer, ClothesListSerializer, ClothesSizeSerializer, ClothesColorSerializer, ClothesInStockSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsClothesOwnerOrReadOnly


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryDetailViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = (permissions.IsAdminUser,)


class ClothesListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Clothes.objects.all()
    serializer_class = ClothesListSerializer
    permission_classes = (IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)


class ClothesSizeListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset= ClothesSize.objects.all()
    serializer_class = ClothesSizeSerializer
    permission_classes = (IsAdminOrReadOnly,)      


class ClothesColorListViewSet(viewsets.ModelViewSet):
    queryset =ClothesColor.objects.all()
    serializer_class = ClothesColorSerializer
    permission_classes = (IsAdminOrReadOnly)      


class ClothesInStockListViewSet(viewsets.ModelViewSet):
    queryset = ClothesInStock.objects.all()
    serializer_class = ClothesInStockSerializer
    permission_classes = (IsAdminOrReadOnly)
