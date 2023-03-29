from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Puoduct)
admin.site.register(Oder)
admin.site.register(OderTtem)
admin.site.register(ShippingAddress)
