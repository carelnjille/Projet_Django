from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quartier/<int:quartier_id>/', views.quartier_detail, name='quartier_detail'),
    path('maison/<int:maison_id>/', views.maison_detail, name='maison_detail'),
    path('creer-quartier/', views.creer_quartier, name='creer_quartier'),
    path('creer-maison/', views.creer_maison, name='creer_maison'),
]