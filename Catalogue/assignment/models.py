from django.db import models

# Create your models here.




class Category(models.Model):
	category_name = models.CharField(max_length=100)
	category_description = models.CharField(max_length=200)
	category_active = models.BooleanField(default=True)


	class Meta:
		db_table = "tb_Category"



class Product(models.Model):
	product_name = models.CharField(max_length=100)
	product_description = models.CharField(max_length=200)
	product_active = models.BooleanField(default=True)
	category = models.ManyToManyField(Category)

	class Meta:
		db_table = "tb_Product"

class Attributes(models.Model):


	attribute_name = models.CharField(max_length=100)
	attribute_description = models.CharField(max_length=200)

	class Meta:
		db_table = "tb_Attributes"


class Product_Attributes(models.Model):

	product = models.OneToOneField(Product, on_delete=models.CASCADE)
	attribute = models.OneToOneField(Attributes, on_delete=models.CASCADE)
	attribute_value = models.CharField(max_length=100)

	class Meta:
		db_table = "tb_Product_Attributes"


class Dealers(models.Model):
	dealer_name = models.CharField(max_length=100)
	dealer_address = models.CharField(max_length=250)
	dealer_phnr = models.IntegerField()
	dealer_active = models.BooleanField(default=True)
	product = models.ManyToManyField(Product)

	class Meta:
		db_table = "tb_Dealer"


class Shop(models.Model):
	shop_name = models.CharField(max_length=100)
	shop_address = models.CharField(max_length=250)
	shop_active = models.BooleanField(default=True)
	dealers = models.ForeignKey(Dealers, on_delete=models.CASCADE)

	class Meta:
		db_table = "tb_Shop"
