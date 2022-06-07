from django.contrib import admin
from .models import User, Client, Agency, Offer, OfferImages, Comment, Favourite

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Agency)
admin.site.register(Offer)
admin.site.register(OfferImages)
admin.site.register(Comment)
admin.site.register(Favourite)

