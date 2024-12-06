from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'dental_management/home.html')


def about(request):
    return render(request, 'dental_management/about.html')