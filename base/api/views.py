from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from ..models import Offer
from .serializers import OfferSerializer

# Create your views here.

def offerList(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    offers = Offer.objects.filter(
        Q(title__contains=q) | 
        Q(description__contains=q)
    )
    serializer = OfferSerializer(offers, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 2})