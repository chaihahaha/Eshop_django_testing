from django.shortcuts import render_to_response
from django.http import HttpResponse
from order.models import Product, Ptype, Order, UserProfile

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render_to_response("index.html",
                              {"user": request.user, "products": products})
