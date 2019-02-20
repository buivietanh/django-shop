from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # if request.user.is_authenticated:
    #     username = request.user.username
    
    username = request.user.username
    title = 'Đây là trang home'
    content = 'Xin chào: ' + username
    template = 'pages/home.html'
    context = locals()
    return render(request, template, context)