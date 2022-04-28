from django.shortcuts import render
from django.http import JsonResponse
from ..models import Offer
from .serializers import OfferSerializer

# Create your views here.

def offerList(request):
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many=True)
    return JsonResponse(serializer.data, safe=False)