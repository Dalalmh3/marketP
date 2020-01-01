from django.db import models

# Create your models here.
class Product(models.Model):
   Product_Name_En= models.CharField(max_length=45)
   Product_Name_Ar= models.CharField(max_length=45)
   description = models.TextField()
   img_url= models.ImageField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __Str__(self):
    return self.Product_Name_En

