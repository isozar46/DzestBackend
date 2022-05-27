from django.urls import include, path
from . import views

urlpatterns = [
    path('offers/', views.offerList),
    path('offer/', views.offer),
    path('offer_images/', views.offerImages),
    
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls'))
]