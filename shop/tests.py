from django.test import TestCase

# Create your tests here.
from .models import Shop, Product, Deal

# Create your views here.
def index(req):
    shops = Shop.objects.all()
    products = Product.objects.all()
    deals = Deal.objects.all()
    context = {
        "shops" : shops,
        "products" : products,
        "deals" : deals
    }
    return render(req, "myapp/index.html", context)