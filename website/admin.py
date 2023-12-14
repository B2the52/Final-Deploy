from django.contrib import admin
from .models import Service, Review, Invoice

# Register your models here.
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(Invoice)