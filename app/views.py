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



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class BotUserViewSet(viewsets.ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    filter_backends = [filters.SearchFilter]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    

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
    



