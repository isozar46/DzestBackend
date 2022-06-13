from django.urls import include, path
from . import views

urlpatterns = [
    path('offers/', views.offerList),
    path('offer/', views.offer),
    path('offer_images/', views.offerImages),

    path('test/', views.ListOffers.as_view()),
    path('add_offer/', views.AddOffer.as_view()),
    path('add_image/', views.AddImage.as_view()),

    path('add_favourite/', views.AddFavourite.as_view()),

    path('user_details/', views.current_user),

    path('delete_offer/<str:pk>', views.offer_delete),

    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/registration/agency/', views.AgencyRegistrationView.as_view(), name='register-agency'),
    path('auth/registration/client/', views.ClientRegistrationView.as_view(), name='register-client'),
]