from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_packs, name='packs'),
    path('<int:pack_id>/', views.pack_detail, name='pack_detail'),
    path('add/', views.add_pack, name='add_pack'),
    path('edit/<int:pack_id>/', views.edit_pack, name='edit_pack'),
    path('delete/<int:pack_id>', views.delete_pack, name='delete_pack'),
]
