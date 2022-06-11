from dataclasses import field
from rest_framework import serializers
from ..models import Offer, OfferImages, Comment, User, Agency, Client
from django.db.models import Q
from django.conf import settings
from dj_rest_auth.registration.serializers import RegisterSerializer


class AgencyIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ('id')


class UserDetailsSerializer(serializers.ModelSerializer):
    agency_id = serializers.PrimaryKeyRelatedField(source='agency', many=False, read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(source='client', many=False, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'agency_id', 'client_id', 'username', 'email', 'is_agency', 'is_client')

class AgencyCustomRegistrationSerializer(RegisterSerializer):
    agency = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    name = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(AgencyCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'name' : self.validated_data.get('name', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(AgencyCustomRegistrationSerializer, self).save(request)
        user.is_agency = True
        user.save()
        agency = Agency(agency=user, name=self.cleaned_data.get('name'),)
        agency.save()
        return user

class ClientCustomRegistrationSerializer(RegisterSerializer):
    client = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    
    def get_cleaned_data(self):
            data = super(ClientCustomRegistrationSerializer, self).get_cleaned_data()
            return data

    def save(self, request):
        user = super(ClientCustomRegistrationSerializer, self).save(request)
        user.is_client = True
        user.save()
        client = Client(client=user,)
        client.save()
        return user

class ImageSerialiser(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = OfferImages
        fields = ('id', 'image_url')
    
    def get_image_url(self, obj):
        return str(settings.SERVER_URL) + '/static' + obj.image.url

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    replies = serializers.SerializerMethodField('sub_comments')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'text', 'created', 'depth', 'refrence', 'replies')
    
    def sub_comments(self, instance):
        comments = Comment.objects.filter(refrence__id=instance.id)
        return CommentSerializer(comments, many=True).data

class SimpleOfferSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.name', read_only=True)
    images = serializers.SerializerMethodField('offer_images')

    class Meta:
        model = Offer
        fields = ['id', 'owner_name', 'title', 'description', 'price', 'created', 'state', 'images']
    
    def offer_images(self, instance):
        images = OfferImages.objects.filter(offer__id=instance.id)
        return ImageSerialiser(images, many=True).data

class DetailedOfferSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.name', read_only=True)
    images = serializers.SerializerMethodField('offer_images')
    comments = serializers.SerializerMethodField('get_comments')

    class Meta:
        model = Offer
        fields = ['id', 'owner_name', 'title', 'description', 'price', 'created', 'state', 'images', 'comments']
    
    def offer_images(self, instance):
        images = OfferImages.objects.filter(offer__id=instance.id)
        return ImageSerialiser(images, many=True).data
    
    def get_comments(self, instance):
        comments = Comment.objects.filter(
            Q(offer__id=instance.id) &
            Q(depth=0)
        )
        return CommentSerializer(comments, many=True).data


class AddOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class AddImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferImages
        fields = '__all__'

    def create(self, validated_data):
        return OfferImages.objects.create(**validated_data)