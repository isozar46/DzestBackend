from django.urls import path
from . import views

urlpatterns = [
    path('offers/', views.offerList),
]