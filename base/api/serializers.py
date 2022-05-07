from rest_framework import serializers
from ..models import Offer
# from django.utils.timesince import timesince

class OfferSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.name', read_only=True)
    # date = serializers.DateTimeField(source='created', read_only=True)
    class Meta:
        model = Offer
        fields = ['id', 'owner_name', 'title', 'description', 'price', 'created', 'state']