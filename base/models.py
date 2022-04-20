from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    register = models.TextField(max_length=50)
    approval = models.TextField(max_length=50)

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    municipal = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    street_adress = models.TextField(max_length=50)

    def __str__(self):
        return "%s, %s, %s" % (self.state, self.municipal, self.street_adress)

class Offer(models.Model):
    owner = models.ForeignKey(Agency, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    transaction_type = models.CharField(max_length=30)
    property_type  = models.CharField(max_length=30)
    property_area = models.CharField(max_length=30)
    negotiability = models.BooleanField()
    notarial_act = models.BooleanField()
    electricity = models.BooleanField()
    gaz = models.BooleanField()
    internet = models.BooleanField()

    def __str__(self):
        return self.title

class OfferImages(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    # image =

    def __str__(self):
        return self.offer.title

class OfferLocation(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    municipal = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    street_adress = models.TextField(max_length=50)
    longtitude = models.FloatField(max_length=50)
    latitude = models.FloatField(max_length=50)

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.state, self.municipal, self.street_adress, self.longtitude, self.latitude)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s: %s, %s" % (self.user, self.text, self.created)

class Follow(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

    def __str__(self):
        return "%s follows %s" % (self.client, self.agency)

class Favourite(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return "%s likes %s" % (self.client, self.offer)



