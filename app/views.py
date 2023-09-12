# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import filters

from .serializers import *
from .models import *
from app.fake_data_generator import *



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def generate_data(request):
    generate_fake_data()
    return HttpResponse('Fake data generated!')


class BotUserViewSet(viewsets.ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    filter_backends = [filters.SearchFilter]
    
    

    # generate fake bot users
    @action(detail=False, methods=['post'])
    def generate_fake_bot_users(self, request):
        generate_bot_users()
        return Response({'status': 'Fake bot users generated!'})
    


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]

    @action(detail=False, methods=['post'])
    def generate_fake_comments(self, request):
        generate_comments()
        return Response({'status': 'Fake comments generated!'})
    


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]

    @action(detail=False, methods=['post'])
    def generate_fake_orders(self, request):
        generate_orders()
        return Response({'status': 'Fake orders generated!'})
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]

    @action(detail=False, methods=['post'])
    def generate_fake_categories(self, request):
        generate_categories()
        return Response({'status': 'Fake categories generated!'})

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = [filters.SearchFilter]

    @action(detail=False, methods=['post'])
    def generate_fake_subcategories(self, request):
        generate_subcategories()
        return Response({'status': 'Fake subcategories generated!'})
    

class OrderHistoryViewSet(viewsets.ModelViewSet):
    queryset = OrderHistory.objects.all()
    serializer_class = OrderHistorySerializer
    filter_backends = [filters.SearchFilter]

    @action(detail=False, methods=['post'])
    def generate_fake_order_histories(self, request):
        generate_order_histories()
        return Response({'status': 'Fake order histories generated!'})

class OrderFileViewSet(viewsets.ModelViewSet):
    queryset = OrderFile.objects.all()
    serializer_class = OrderFileSerializer
    filter_backends = [filters.SearchFilter]

    @action(detail=False, methods=['post'])
    def generate_fake_order_files(self, request):
        generate_order_files()
        return Response({'status': 'Fake order files generated!'})
    
    

from rest_framework.views import APIView

class ChangeLanguage(APIView):
    def post(self, request):
        if not request.method == 'POST':
            return Response({'status': 'Method not allowed!'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        data = request.data
        telegram_id = data.get('telegram_id', None)
        
        try:
            user = BotUser.objects.get(telegram_id=telegram_id)
        except BotUser.DoesNotExist:
            return Response({'status': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.language = data.get('language', user.language)
        user.save()
        return Response({'status': 'Language changed!'})
    
class ChangePhoneNumber(APIView):
    def post(self, request):
        data = request.POST
        data = data.dict()
        telegram_id = data.get('telegram_id')
        user = BotUser.objects.get(telegram_id=telegram_id)
        user.phone = data.get('phone')
        user.save()
        return Response({'status': 'Phone number changed!'})
    



