from django.urls import path
from . import views
from .webhooks import my_webhook_view

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('wh/', my_webhook_view, name='webhook'),
]
