from django.urls import path
from .views import OutflowListView, OutflowCreateView, OutflowDetailView, OutflowRetriveApiView, OutflowListCreateApiView


urlpatterns = [
    path('outflows/create/', OutflowCreateView.as_view(), name='outflow_create'),
    path('outflows/list/', OutflowListView.as_view(), name='outflow_list'),
    path('outflows/<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),

    path('api/v1/outflows/', OutflowListCreateApiView.as_view(), name='outflow-creat-list-api-view'),
    path('api/v1/outflows/<int:pk>/', OutflowRetriveApiView.as_view(), name='outflow-detail-api-view'),

]
