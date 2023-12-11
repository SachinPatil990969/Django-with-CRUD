from django.urls import path
from .views import *

urlpatterns = [
    path('', item_list, name='item_list'),
    path('item/<int:pk>/', item_detail, name='item_detail'),
    path('item/new/', item_new, name='item_new'),
    path('item/<int:pk>/edit/', item_edit, name='item_edit'),
    path('item/<int:pk>/delete/', item_delete, name='item_delete'),
]
