# billing/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_page, name='billing_page'),
    path('generate_bill/', views.generate_bill, name='generate_bill'),
    path('previous_purchases/', views.previous_purchases, name='previous_purchases'),
    path('add-product/', views.add_product, name='add_product'),
    #path('view-bill/<int:bill_id>/', views.view_bill, name='view_bill'),
    path('products/', views.product_list, name='product_list'),
]
