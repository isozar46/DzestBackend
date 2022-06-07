from django.urls import include, path
from . import views

urlpatterns = [
    path('offers/', views.offerList),
    path('offer/', views.offer),
    path('offer_images/', views.offerImages),

    path('test/', views.ListOffers.as_view()),
    path('add_offer/', views.AddOffer.as_view()),
    path('add_image/', views.AddImage.as_view()),
    
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls'))
]