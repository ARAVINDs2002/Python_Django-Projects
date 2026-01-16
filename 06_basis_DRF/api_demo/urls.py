from django.urls import path
from . import views

urlpatterns = [
    # JSON API endpoint
    path('api/items/', views.ItemListAPIView.as_view(), name='item-api'),
    
    # HTML View endpoint (rendered via DRF)
    path('items/', views.ItemListWebView.as_view(), name='item-web'),
]
