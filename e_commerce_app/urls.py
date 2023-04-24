#On y fix les routes de l'API REST
#On utilise la classe DefaultRouter de DRF(Django Rest Framework)
#DefaultRouter retourne une reference sur les routes definies par DRF
#On ajoute (en enregistre) à DefaultRouter les routes de notre API REST
#On utilise la methode register() de DefaultRouter pour enregistrer les routes

from rest_framework import routers
from .views import ProductViewSet, ClientViewSet
from django.urls import path, include
router=routers.DefaultRouter()
router.register('products',ProductViewSet)
router.register('clients',ClientViewSet)

urlpatterns = [
    path('',include(router.urls)),
]