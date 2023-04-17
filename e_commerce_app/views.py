from django.shortcuts import render

# Create your views here.
#On va implementer l'API REST dans ce fichier en utilisant viewsets.ModelViewSet
#viewsets.ModelViewSet est une classe de base fournie par DRF(Django Rest Framework)
#qui permet de creer des API REST et surtout le CRUD d'une manère très simple.
#pour implementer le CRUD via cette classe, il suffit de preciser:
#Le queryset : c'est l'ensemble des objets de la base de données à manipuler
# et la classe de serialisation: c'est la classe qui permet de transformer les objets python en json et vis versa

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
