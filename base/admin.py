from django.contrib import admin
from .models import Client, Agency, Offer, OfferImages, Comment

# Register your models here.
admin.site.register(Client)
admin.site.register(Agency)
admin.site.register(Offer)
admin.site.register(OfferImages)
admin.site.register(Comment)

