from rest_framework import serializers
from .models import *

class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField(read_only=True, many=True)
    class Meta:
        model = Order
        fields = '__all__'

class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistory
        fields = '__all__'

class OrderFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFile
        fields = '__all__'
    
class CategorySerializer(serializers.ModelSerializer):
    subcategory = serializers.SerializerMethodField(read_only=True, many=True)
    orders = serializers.SerializerMethodField(read_only=True, many=True)
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField(read_only=True, many=True)
    class Meta:
        model = Subcategory
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'




