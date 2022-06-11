from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_agency = models.BooleanField(default=False)

    email = models.EmailField(unique=True,null=False)
    avatar = models.ImageField(null=True, upload_to='avatars', default='defaults/default-avatar.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Agency(models.Model):
    agency = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    state = models.CharField(max_length=50, null=True)
    municipal = models.CharField(max_length=50, null=True)
    street_adress = models.TextField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Offer(models.Model):
    owner = models.ForeignKey(Agency, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()

    OFFER_TYPE_CHOICES = (
      ('Apartement', 'Apartement'),
      ('Offices and businesses', 'Offices and businesses'),
      ('Land', 'Land'),
    )
    property_type = models.TextField(choices=OFFER_TYPE_CHOICES, null=True)

    TRANS_TYPE_CHOICES = (
      ('Rent', 'Rent'),
      ('Sale', 'Sale'),
    )
    transaction_type = models.TextField(choices=TRANS_TYPE_CHOICES, null=True)

    property_area = models.IntegerField(null=True)
    
    # offer location
    state = models.CharField(max_length=50,)
    municipal = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    street_adress = models.TextField(max_length=50)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title

class OfferImages(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='offer_images')

    def __str__(self):
        return self.offer.title

class Client(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.client.username)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    depth = models.IntegerField(default=0)
    refrence = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s, %s" % (self.user, self.text, self.created)


class Favourite(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return "%s likes %s" % (self.client, self.offer)



