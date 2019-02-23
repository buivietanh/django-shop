from django.shortcuts import render, Http404
from . models import Product

# Create your views here.
def index(request):
    name = request.user.username
    template = 'pages/product.html'
    context = locals()

    return render(request, template, context)

def all(request):
    products = Product.objects.all()
    name = request.user.username
    template = 'pages/all_product.html'
    context = locals()

    return render(request, template, context)

def single(request, slug):
    try:
        product = Product.objects.get(slug = slug)
        template = 'pages/single.html'
        context = locals()

        return render(request, template, context)
    except Product.DoesNotExist:
        raise Http404
    
def search(request):
    try:
        field_keyword = request.GET['field-keyword']
    except :
        field_keyword = None
    if field_keyword:
        results = Product.objects.filter(title__icontains=field_keyword)
        query = field_keyword
        template = 'pages/search.html'
        context = locals()
    else:
        print(field_keyword)
        template = 'pages/all_product.html'
        context = locals()
    return render(request, template, context)
    