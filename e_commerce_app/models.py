from django.db import models

# Create your models here.
from django.db import models
from datetime import  date
from django.utils import timezone
# Create your models here.
#define an enumeration for the client type
class ClientType(models.TextChoices):
    normal=('NORMAL','normal customer')
    loyal=('LOYAL','loyal customer')
    vip=('VIP','Very Important Customer')
    
class User(models.Model):
    name=models.CharField(max_length=50,default='')
    email=models.EmailField(max_length=254,default='')
    password=models.CharField(max_length=50,default='')
    phone_number=models.CharField(max_length=20,default='')
    class Meta:
        #The ORM will not create a table for this model
        abstract=True
        #Users are ordered by name in ascendening order and then by email
        #in descending order
        ordering=['name','-email']
    def __str__(self):
        return f'name = {self.name} email = {self.email} phone_number = {self.phone_number}'
class Address(models.Model):
    houseNumber=models.PositiveSmallIntegerField(default=0)
    street = models.CharField(max_length=50,default='')
    city = models.CharField(max_length=50,default='')
    country = models.CharField(max_length=50,default='')
    postalCode = models.CharField(max_length=50,default='')
    class Meta:
        db_table = 'address'
        ordering=['country','city']
class Product(models.Model):
    label = models.CharField(max_length=50,default='',unique=True)
    price = models.FloatField(default=0)
    expirationDate = models.DateField(default=date(2023,12,31))
    manufacturingDate= models.DateField(default=timezone.now)
    stock=models.PositiveSmallIntegerField(default=0)
    photo=models.ImageField(upload_to='photos/product_photos',null=True,blank=True)
    description = models.TextField(max_length=200,null=True,blank=True)
    provider = models.ForeignKey('Provider',on_delete=models.SET_NULL,null=True,blank=True)
    class Meta:
        db_table = 'products'
        ordering=['label','price']
    def __str__(self):
        #return 'label = ',self.label,'price = ',self.price,'stock = ',self.stock
        #return f'label = {self.label} price = {self.price} stock = {self.stock}'
        #return 'label = {} price = {} stock = {}'.format(self.label,self.price,self.stock)
        return 'label = %s price = %s stock = %s'%(self.label,self.price,self.stock)
class Client(User):
    lastName = models.CharField(max_length=50,default='')
    #clientType=models.CharField(max_length=50,choices=[('NORMAL','normal customer'),('LOYAL','loyal customer'),('VIP','Very Important Customer')],default='NORMAL')
    #or we can use the enumeration
    clientType=models.CharField(max_length=50,choices=ClientType.choices,default=ClientType.normal)
    address = models.OneToOneField(Address,on_delete=models.CASCADE)
    clientProducts=models.ManyToManyField(Product,through='Command',through_fields=('client','product'))
    class Meta:
        db_table = 'clients'
        ordering=['lastName','name']
    def __str__(self):
        return super().__str__()+f' lastName = {self.lastName} clientType = {self.clientType}'
class Provider(User):
    site_url=models.URLField(max_length=200,default='')
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        db_table = 'providers'

class Command(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date_cmd = models.DateTimeField(default=timezone.now)
    quantity = models.PositiveSmallIntegerField(default=1)
    class Meta:
        db_table = 'command'
        ordering=['-date_cmd',]
        #The verbose_name and verbose_name_plural attributes are used to give a more human-readable name to the model
        verbose_name='Command Management',
        verbose_name_plural='Command List'
        unique_together = [('client','product','date_cmd')]
        

