from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from ..models import Offer, OfferImages
from .serializers import SimpleOfferSerializer, DetailedOfferSerializer, ImageSerialiser

# Create your views here.

def offerList(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    offers = Offer.objects.filter(
        Q(title__contains=q) | 
        Q(description__contains=q)
    )
    serializer = SimpleOfferSerializer(offers, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 2})

def offer(request):
    id = request.GET.get('id')
    offer = Offer.objects.get(id=id)
    serializer = DetailedOfferSerializer(offer, many=False)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 2})

def offerImages(request):
    id = request.GET.get('id')
    image = OfferImages.objects.filter(offer__id=id)
    serializer = ImageSerialiser(image, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 2})