from django.urls import path
from .views import AddItemView, ItemListView

urlpatterns = [
    path('add_item/', AddItemView.as_view(), name='add_item'),
    path('item_list/', ItemListView.as_view(), name='item_list'),
]
