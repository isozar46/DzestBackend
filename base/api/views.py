from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from ..models import Offer, OfferImages, Favourite, Client
from .serializers import (AddImageSerializer, SimpleOfferSerializer, DetailedOfferSerializer,
                          ImageSerialiser, AddOfferSerializer, AgencyCustomRegistrationSerializer,
                          ClientCustomRegistrationSerializer, UserDetailsSerializer,
                          AddFavouriteSerializer,)
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.pagination import PageNumberPagination
from dj_rest_auth.registration.views import RegisterView
# Create your views here.


class AgencyRegistrationView(RegisterView):
    serializer_class = AgencyCustomRegistrationSerializer


class ClientRegistrationView(RegisterView):
    serializer_class = ClientCustomRegistrationSerializer


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


class AddOffer(mixins.CreateModelMixin, generics.GenericAPIView):
    # permission_classes = []
    # authentication_classes = []
    queryset = Offer.objects.none()
    serializer_class = AddOfferSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListOffers(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Offer.objects.all()
    serializer_class = SimpleOfferSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# class ListOffers(APIView):
#     permission_classes = []
#     authentication_classes = []
#     pagination_class = PageNumberPagination

#     def get(self, request, format=None):
#         offers = Offer.objects.all()
#         paginator = PageNumberPagination()
#         page = paginator.paginate_queryset(offers, request)
#         serializer = SimpleOfferSerializer(page, many=True)
#         return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)


class AddImage(APIView):
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        serializer = AddImageSerializer(data=request.data)
        if serializer.is_valid():
            image = request.data.get('image')
            serializer.save(
                offer=Offer.objects.get(id=request.data.get('offer')),
                image=image
            )
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def my_offers(request):

@api_view(['GET'])
def current_user(request):
    serializer = UserDetailsSerializer(request.user)
    return Response(serializer.data)


# @api_view(['GET'])
# def current_user(request):
#     user = request.user
#     return Response({
#         'user_id': user.id,
#         'username': user.username,
#         'email': user.email,
#         'is_client': user.is_client,
#         'is_agency': user.is_agency
# })

class AddFavourite(mixins.CreateModelMixin, generics.GenericAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    queryset = Favourite.objects.none()
    serializer_class = AddFavouriteSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@api_view(['DELETE'])
def offer_delete(request, pk):
    try:
        offer = Offer.objects.get(id=pk)
    except Offer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# test
