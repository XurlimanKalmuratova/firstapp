from django.urls import path
from .views import (
    home, 
    repairs, 
    about, 
    sale,
    sale_detail,
    sale_create,
    sale_delete,
    sale_update
)

urlpatterns = [
    path('', home, name='home'),
    path('sale/', sale, name='sale'),
    path('sale/<int:pk>/', sale_detail, name='sale_detail'),
    path('sale/<pk>/delete/', sale_delete, name='sale_delete'),
    path('sale/<pk>/update/', sale_update, name='sale_update'),
    path('repairs/', repairs, name='repairs'),
    path('about/', about, name='about'),
    path('create/', sale_create, name='create'),
]
