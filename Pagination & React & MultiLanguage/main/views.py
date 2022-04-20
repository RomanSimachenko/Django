from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
from django.utils.translation import gettext as _


def IndexView(request):
    """Main page"""
    amount = request.GET.get('amount', default=20)
    products = models.Product.objects.all()
    paginator = Paginator(products, amount)
    page_number = request.GET.get('page', default=1)
    pagination_products = paginator.get_page(page_number)

    return render(request, 'main/index.html', {'products': pagination_products})
