from django.shortcuts import render

# Create your views here.
#On va implementer l'API REST dans ce fichier en utilisant viewsets.ModelViewSet
#viewsets.ModelViewSet est une classe de base fournie par DRF(Django Rest Framework)
#qui permet de creer des API REST et surtout le CRUD d'une manère très simple.
#pour implementer le CRUD via cette classe, il suffit de preciser:
#Le queryset : c'est l'ensemble des objets de la base de données à manipuler
# et la classe de serialisation: c'est la classe qui permet de transformer les objets python en json et vis versa

#Queleques methodes dans Django pour assurer le CRUD ou autre actions personalisées
#1- result=Product.objects.all() : retourne tous les objets de la table Product (select * from Product)
#2- result=Product.objects.get(id=1) : retourne l'objet de la table Product dont l'id est 1 (select * from Product where id=1)
#ou bien on peut aussi ecrire result=Product.objects.get(pk=1)
#3- result=Product.objects.filter(label='milk') : retourne tous les objets de la table Product dont le label est 'milk' (select * from Product where label='milk')
#4- result=Product.objects.filter(label__contains='l') : retourne tous les objets de la table Product dont le label contient 'l' (select * from Product where label like '%l%')
#Il existe auusi des autres operateurs
# __icontains: ignore la casse
# __gt: >
# __gte: >=
# __lt: <
# __lte: <=
#__exact ou iexact : (==)
#__in : select * product where id in (1,2,3) => en django Product.objects.filter(id__in=[1,2,3])
#__startswith ou endswith
#5- result=Product.objects.filter(label__contains('milk')).first() : retourne le premier objet de la table Product dont le label est 'milk' (select * from Product where label='milk' limit 1)
#6- result=Product.objects.filter(label__contains('milk')).last() : retourne le dernier objet de la table Product dont le label est 'milk' (select * from Product where label='milk' order by id desc limit 1)
#7- result=Product.objects.filter(label__contains('milk')).order_by('price') : retourne tous les objets de la table Product dont le label contient 'milk' et les trier par prix (select * from Product where label like'%milk%' order by price)
#8- retourner les produits qui n'ont pas encore un prix :
#result=Product.objects.filter(price__isnull=True)
#Exemple utilisant exclude, values(), distinct(), count() et aggregate()
#exculde : inverse de filter()
#Recupere les produits créer avant 2021
#result=Product.objects.exclude(manufacturingDate__year__gte=2021)
#values() : permet de retourner le resultat en le projetant sur quelques champs
#result=Product.objects.values('label','price') ==>en SQL select label, price from Product
#distinct() : permet de retourner le resultat sans doublons
#result=Product.objects.distinct('manufacturingDate__year')
#count() : permet de retourner le nombre d'objets
#aficher le nombre de produits primés
#result=Product.objects.filter(experationDate__lt='17-04-2023').count()
#aggregate() : permet de retourner le resultat d'une fonction d'agregation (min, max, avg, sum)
#selectioner le maximum et le minimum des prix des produits
#result=Product.objects.aggregate(Max('price'),Min('price'))
from .models import Product, Client,Command
from .serializers import ProductSerializer, ClientSerializer, CommandSerializer
from rest_framework import viewsets
class ProductViewSet(viewsets.ModelViewSet):
    #par defaut, toutes les methodes HTTP seront implementées(POST, GET, PUT, DELETE, PATCH) 
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    #without http_method_names, methods GET, POST, PUT, PATCH and DELETE will be implemented
    #personaliser le traitement, en precisant les methodes HTTP à implementer
    #http_method_names=['get','post','delete']

class CommandViewSet(viewsets.ModelViewSet):
    queryset=Command.objects.all()
    serializer_class=CommandSerializer
