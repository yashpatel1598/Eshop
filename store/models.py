from django.db import models

# Create your models here.

class  Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def getall_category():
        return Category.objects.all()

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
    
    @staticmethod
    def getall_prodcuts_by_id(category_id):
        if category_id:
            return Product.objects.filter(Category = category_id)
        else :
            return Product.objects.all()

class Customer(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=15)
    password = models.CharField(max_length=200)

    def  __str__(self):
        return f'{self.firstName} {self.lastName}'

    @staticmethod
    def createCustomer(customerData):
        newCustomer = Customer(**customerData)
        newCustomer.save()
        return newCustomer
    
    @staticmethod
    def checkemail(email):
        customerByEmail = Customer.objects.filter(email = email).first()
        if customerByEmail:
            return customerByEmail
        else:
            return False
