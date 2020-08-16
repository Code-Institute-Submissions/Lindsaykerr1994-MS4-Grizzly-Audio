from django.urls import path
from . import views
from .webhooks import my_webhook_view

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_no_payment', views.checkout_no_payment, name="checkout_no_payment"),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data,
         name='cache_checkout_data'),
    path('wh/', my_webhook_view, name='webhook'),
]
