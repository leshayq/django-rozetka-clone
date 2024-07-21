from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404

from .models import Category, ProductProxy, Product

from django.core.paginator import Paginator
from django.views.generic.list import ListView


class ProductsView(ListView):
    model = ProductProxy
    template_name = 'shop/products.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context

# def products_view(request):
#     products = ProductProxy.objects.all()
#     paginator = Paginator(products, 12)
    
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'shop/products.html', {'products': products, 'page_obj': page_obj})

def products_detail_view(request, slug):
    product = get_object_or_404(ProductProxy, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})

def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = ProductProxy.objects.select_related('category').filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, 'shop/category_list.html', context)
