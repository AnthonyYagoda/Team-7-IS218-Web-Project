from django.contrib import admin

# Register your models here.
from django.contrib import admin

from hello.models import Product, Feedback

# Register your models here.
admin.site.register(Product)
admin.site.register(Feedback)

