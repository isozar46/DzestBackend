from django.contrib import admin
from .models import Client, Agency, Offer

# Register your models here.
admin.site.register(Client)
admin.site.register(Agency)
admin.site.register(Offer)
