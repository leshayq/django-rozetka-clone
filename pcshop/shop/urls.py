from django.urls import path
from .views import products_detail_view, ProductsView, category_list

app_name = 'shop'

urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('<slug:slug>/', products_detail_view, name='product_detail'),
    path('search/<slug:slug>/', category_list, name='category_list'),
]
