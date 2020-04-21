from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import ListView 
from django.db.models import Q
from django.urls import reverse_lazy
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import ProductFilter


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    page = request.GET.get('page', 1) 
    paginator = Paginator(products, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
        
    }
    
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)
   
  
class SearchResultsView(ListView):
    model = Product
    template_name = 'search.html'
    def get_queryset(self):
        query=self.request.GET.get('q') 
        product_list =Product.objects.filter(Q(name__icontains=query) | Q(price__icontains=query))
        return product_list
        