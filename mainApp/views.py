from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'mainApp/home.html')


def contact(request):
    return render(request, 'mainApp/contact.html', {'values': ['call me: ', '8(999)148-00-11']})
