#On definit une classe de Serialisation pour chaque model
#Product, Client, Provider, Command, Address
#Une classe de serialisation doit heriter de serialiers.ModelSerializer
#Le role d'une classe de serialisation est de transformer
# Les objets python en json et vis versa
from rest_framework import serializers
from .models import Product, Client, Command
#Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' #tous les chapms du modèle Product seront serialiser
        #fields=('label','price','stock') #on peut aussi choisir les champs à serialiser

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'