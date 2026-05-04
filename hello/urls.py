from django.urls import path
from hello import views


urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<str:name>/", views.hello_there, name="hello_there"), # Lab 2 - Add a URL pattern for the hello_there view that captures a string parameter called name
    path("DrinkList/", views.DrinkList, name="DrinkList"), # Lab 2 - Add a URL pattern for the about view
    path("DrinkInformation/", views.DrinkInformation, name="DrinkInformation"), # Lab 2 - Add a URL pattern for the contact view
    path("Feedback/<int:product_id>/", views.product_feedback, name="Feedback"),#Lab 3 - Add a URL pattern for the product_feedback view that captures an integer parameter called product_id
    
]