from django.db import models
from django.utils import timezone #Lab 3.

#Feedback Form Stuff:
#Defines a Product model with fields for name, description, price, and image URL.
class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_range = models.CharField(max_length=50, blank=True)
    image = models.URLField(blank=True)
    
#Returns String of data present in Product model.
    def __str__(self):
        return self.name

#Feedback model that has a foreign key relationship to Product, as well as fields for ratings, comments, and submission time.
class Feedback(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedback')
    ratings = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comments = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

#Returns String of data present in Feedback model.
    def __str__(self):
        return f"Rating {self.ratings}/5 for {self.product.name}"
