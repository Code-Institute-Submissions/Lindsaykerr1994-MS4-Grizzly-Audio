from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_packs, name='packs'),
    path('<pack_id>', views.pack_detail, name='pack_detail'),
]
