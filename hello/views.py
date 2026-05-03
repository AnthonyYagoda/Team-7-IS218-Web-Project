from itertools import product
from urllib import request

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render # Lab 2 - Import the render function to render templates
from datetime import datetime # Lab 2 - Import the datetime module to get the current date and time

from hello.forms import FeedbackForm #Lab 3 Feedback Form Stuff - Import the FeedbackForm class from the forms.py file in the hello app
from hello.models import Product, Feedback #Lab 3 Feedback Form Stuff - Import the Product and Feedback models from the models.py file in the hello app
from django.views.generic import ListView #Lab 3 Feedback Form Stuff - Import the ListView class from django

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


#Lab 3 Feeedback System Stuff:
def product_feedback(request, product_id):
    product = Product.objects.get(id=product_id) #Identifies the product based on the id in the URL
    products = Product.objects.all() #gets all products to display on feedback page
    feedback_list = Feedback.objects.filter(product=product) #filters feedback to only show feedback for the selected product

#Lab 3 Feedback Form method that handles both GET and POST requests.
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.product = product
            fb.save()
            return redirect("Feedback", product_id=product.id)
    else:
        form = FeedbackForm()

#Renders the Feedback.html template and passes the product, products, feedback_list, and form variables to it.
    return render(request, "hello/Feedback.html", 
    {   
        "products": products,
        "product": product,
        "feedback_list": feedback_list,
        "form": form,
    })
