from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, CategoryListCreateApiView, CategoryRetriveUpdateDestroyApiView


urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/detail/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('api/v1/category/', CategoryListCreateApiView.as_view(), name='category-creat-list-api-view'),
    path('api/v1/category/<int:pk>', CategoryRetriveUpdateDestroyApiView.as_view(), name='category-detail-api-view'),

]
