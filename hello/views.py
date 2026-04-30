from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render # Lab 2 - Import the render function to render templates
from datetime import datetime # Lab 2 - Import the datetime module to get the current date and time

# Create your views here.

def home(request):
    return render(request, "hello/home.html") # Lab 2 - Render the home.html template for the home view
    #return HttpResponse("Hello, Django! My name is Anthony Yagoda, it is April 6, 2026, and I am learning Django in IS 218-004 - Web Application Development at NJIT.") // OLD from Lab 1

def DrinkList(request):
    # Lab 2 - Render the about.html template for the about view
    return render(request, "hello/Drink_List.html")

def DrinkInformation(request):
    # Lab 2 - Render the contact.html template for the contact view
    return render(request, "hello/Drink_Information.html")

def hello_there(request, name):
    # Lab 2 - Render the hello_there.html template and pass the name variable to it
    print(request.build_absolute_uri()) # optional - prints the full URL of the request to the console for debugging purposes
    return render(request, 'hello\hello_there.html', {'name': name, 'date': datetime.now()})
