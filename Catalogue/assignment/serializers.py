from assignment.models import Attributes,Product,Category,Product_Attributes

from rest_framework import serializers

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ('id','attribute_name','attribute_description')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category_name','category_description','category_active')

class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=True ,read_only=True)
    class Meta:
        model = Product
        fields = ('id','product_name','product_description','product_active','category')


