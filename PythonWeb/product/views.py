from django.shortcuts import render

# Create your views here.
def index(request):
    name = request.user.username
    template = 'pages/product.html'
    context = locals()

    return render(request, template, context)