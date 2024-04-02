from django.urls import path
from .views import view_cart, add_to_cart, remove_from_cart, checkout

app_name = "cart"

urlpatterns = [
    path('', view_cart, name="view_cart"),
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/<int:item_id>/', checkout, name="checkout"),
]
    