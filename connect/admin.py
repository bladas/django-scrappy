from django.contrib import admin

# Register your models here.
from .models import Car,CarModel,Brand


admin.site.register(Car)
admin.site.register(CarModel)
admin.site.register(Brand)