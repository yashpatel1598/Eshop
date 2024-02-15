from django.db import models

# Create your models here.

class  Category(models.Model):
    name = models.CharField(max_length=20)

    def  __str__(self):
        return  self.name

class  Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,null=True, blank=True,default = '')
    image = models.ImageField(upload_to= 'product_image/')

    def __str__(self):
        return  self.name + " - $" + str(self.price) + str(self.category)

    @staticmethod
    def getall_prodcuts():
        return Product.objects.all()

