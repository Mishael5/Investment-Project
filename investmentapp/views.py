from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    # Your logic here, if needed
    return render(request, 'investmentapp/index.html')


def about(request):
    # Your logic here, if needed
    return render(request, 'investmentapp/about.html')


def base(request):
    # Your logic here, if needed
    return render(request, 'investmentapp/base.html')
