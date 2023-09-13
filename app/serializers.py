from rest_framework import serializers
from .models import *

class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'


class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistory
        fields = '__all__'

class OrderFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFile
        fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
    files = OrderFileSerializer(read_only=True, many=True)
    class Meta:
        model = Order
        fields = '__all__'
    

class SubCategorySerializer(serializers.ModelSerializer):
    orders = OrderSerializer(read_only=True, many=True)
    class Meta:
        model = Subcategory
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True, read_only=True)
    orders = OrderSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = '__all__'




