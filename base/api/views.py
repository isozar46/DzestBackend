from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from ..models import Offer, OfferImages
from .serializers import AddImageSerializer, SimpleOfferSerializer, DetailedOfferSerializer, ImageSerialiser, AddOfferSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser

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

class AddOffer(mixins.CreateModelMixin,generics.GenericAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Offer.objects.none()
    serializer_class = AddOfferSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ListOffers(mixins.ListModelMixin,generics.GenericAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Offer.objects.all()
    serializer_class = SimpleOfferSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class AddImage(APIView):
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        serializer = AddImageSerializer(data=request.data)
        if serializer.is_valid():
            image=request.data.get('image')
            serializer.save(
                offer=Offer.objects.get(id=request.data.get('offer')),
                image=image
            )
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
