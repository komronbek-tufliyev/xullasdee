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

from django.shortcuts import redirect


def index(request):
    # if requested user is admin then redirect to admin page
    # if request.user.is_superuser:
    #     return redirect('/admin/')
    return redirect('schema-swagger-ui')

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
        
        try:
            telegram_id = data.get('telegram_id', None)
            user = BotUser.objects.get(telegram_id=telegram_id)
            print(user)
        except BotUser.DoesNotExist:
            return Response({'status': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.language = data.get('language', user.language)
        user.save()
        return Response({'status': 'Language changed!'})
    

class GetLanguageView(APIView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        
        if 'telegram_id' not in data:
            return Response({'status': 'telegram_id is required!'}, status=status.HTTP_400_BAD_REQUEST)
        telegram_id: int = data.get('telegram_id', None)
        
        try:
            LANGUAGE = BotUser.objects.only('language').get(telegram_id=telegram_id)
            print(LANGUAGE)
            return Response(BotUserSerializer(LANGUAGE).data)
        except BotUser.DoesNotExist:
            return Response({'status': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print({'status': str(e)})
            return Response({'status': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChangePhoneNumber(APIView):
    def post(self, request):
        if not request.method == 'POST':
            return Response({'status': 'Method not allowed!'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        data = request.data
        if not data.get('telegram_id'):
            return Response({'status': 'telegram_id is required!'}, status=status.HTTP_400_BAD_REQUEST)
        if not data.get('phone_number'):
            return Response({'status': 'phone_number is required!'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            telegram_id = int(data.get('telegram_id'))
            print(telegram_id, type(telegram_id))
            user = get_object_or_404(BotUser, telegram_id=telegram_id)
            user.phone_number = data.get('phone_number')
            user.save()
            return Response({'status': 'Phone number changed!'}, status=status.HTTP_200_OK)
        except BotUser.DoesNotExist:
            return Response({'status': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({'status': 'Invalid telegram_id format!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class MyOrdersView(APIView):
    def get(self, request):
        data = request.data
        try:
            telegram_id = data.get('telegram_id')
            user = BotUser.objects.get(telegram_id=telegram_id)
            orders = Order.objects.filter(user=user)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        except BotUser.DoesNotExist:
            return Response({'status': 'User not found!'})
        except Exception as e:
            print({'status': str(e)})
            pass

class SetOrderView(APIView):
    def post(self, request):
        data = request.POST
        data = data.dict()
        try:
            telegram_id = data.get('telegram_id')
            user = BotUser.objects.get(telegram_id=telegram_id)
            # order info
            order, created = Order.objects.get_or_create(user=user)
            order.type = data.get('type')
            order.category = Category.objects.get(id=data.get('category'))
            order.subcategory = Subcategory.objects.get(id=data.get('subcategory'))
            order.description = data.get('description')
            order.user = user
            order.save()

            # order item info
            order_item, created = OrderItem.objects.get_or_create(order=order)
            order_item.order = order
            order_item.name = data.get('name')
            order_item.duration = data.get('duration')
            order_item.price = data.get('price')
            order_item.save()

            # order files info
            files = request.FILES.getlist('files')
            for file in files:
                OrderFile.objects.create(order=order, file=file)

            return Response({'status': 'Order set!'})
        except BotUser.DoesNotExist:
            return Response({'status': 'User not found!'})
        except Category.DoesNotExist:
            return Response({'status': 'Category not found!'})
        except Subcategory.DoesNotExist:
            return Response({'status': 'Subcategory not found!'})
        except Exception as e:
            print({'status': str(e)})
            pass
        return Response({'status': 'Order not set!'})

class ChangeOrderStatusView(APIView):
    def post(self, request):
        data = request.POST
        data = data.dict()
        telegram_id = data.get('telegram_id')
        user = BotUser.objects.get(telegram_id=telegram_id)
        order = Order.objects.get(id=data.get('order_id'))
        order.status = data.get('status')
        order.save()
        return Response({'status': 'Order status changed!'})
    

class SetOrderHistoryView(APIView):
    def post(self, request):
        data = request.POST
        data = data.dict()
        telegram_id = data.get('telegram_id')
        user = BotUser.objects.get(telegram_id=telegram_id)
        order = Order.objects.get(id=data.get('order_id'))
        OrderHistory.objects.create(order=order, status=data.get('status'))
        return Response({'status': 'Order history created!'})

class GetOrderHistoryView(APIView):
    def get(self, request):
        data = request.GET
        data = data.dict()
        telegram_id = data.get('telegram_id')
        user = BotUser.objects.get(telegram_id=telegram_id)
        order = Order.objects.get(id=data.get('order_id'))
        order_history = OrderHistory.objects.filter(order=order)
        serializer = OrderHistorySerializer(order_history, many=True)
        return Response(serializer.data)
    

class CheckOrderStatusView(APIView):
    def get(self, request):
        data = request.GET
        data = data.dict()
        # telegram_id = data.get('telegram_id')
        # order_id = data.get('order_id')
        # user = BotUser.objects.get(telegram_id=telegram_id)
        order = get_object_or_404(Order, id=data.get('order_id'))
        return Response({'status': order.status})
    
class DeleteOrderView(APIView):
    def delete(self, request):
        data = request.POST
        data = data.dict()
        telegram_id = data.get('telegram_id')
        user = BotUser.objects.get(telegram_id=telegram_id)
        order = Order.objects.get(id=data.get('order_id'))
        order.delete()
        return Response({'status': 'Order deleted!'})
    
class GetOrderFilesView(APIView):
    def get(self, request):
        data = request.GET
        data = data.dict()
        # telegram_id = data.get('telegram_id')
        # user = BotUser.objects.get(telegram_id=telegram_id)
        try:
            order = Order.objects.get(id=data.get('order_id'))
            order_files = OrderFile.objects.filter(order=order)
            serializer = OrderFileSerializer(order_files, many=True)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({'status': 'Order not found!'})
        except Exception as e:
            print({'status': str(e)})
            pass
        return Response({'status': 'Order files not found!'})
    
    
####### Change Order Files #######
class ChangeOrderFilesView(APIView):
    def post(self, request):
        """"
        Change order files
        """
        data = request.POST
        data = data.dict()
        telegram_id = data.get('telegram_id')
        try:
            user = BotUser.objects.get(telegram_id=telegram_id)
            order = Order.objects.get(id=data.get('order_id'))
            files = request.FILES.getlist('files')
            for file in files:
                OrderFile.objects.create(order=order, file=file)
        except Order.DoesNotExist:
            return Response({'status': 'Order not found!'})
        except BotUser.DoesNotExist:
            return Response({'status': 'User not found!'})
        except Exception as e:
            print({'status': str(e)})
            pass

        return Response({'status': 'Order files changed!'})
    
###### Change Order Item #####
class ChangeOrderItemView(APIView):
    def post(self, request):
        data = request.POST
        data = data.dict()
        # telegram_id = data.get('telegram_id')
        # user = BotUser.objects.get(telegram_id=telegram_id)
        try:
            order = Order.objects.get(id=data.get('order_id'))
            order_item = OrderItem.objects.get(order=order)
            order_item.name = data.get('name')
            order_item.duration = data.get('duration')
            order_item.price = data.get('price')
            order_item.save()
        except Order.DoesNotExist:
            return Response({'status': 'Order not found!'})
        except OrderItem.DoesNotExist:
            return Response({'status': 'Order item not found!'})
        except Exception as e:
            print({'status': str(e)})
            pass

        return Response({'status': 'Order item changed!'})
    

#####   Payment  (Create Payment History) #####
class PaymentView(APIView):
    def post(self, request):
        data = request.POST
        data = data.dict()
        telegram_id = data.get('telegram_id')
        user = BotUser.objects.get(telegram_id=telegram_id)
        order = Order.objects.get(id=data.get('order_id'))
        PaymentHistory.objects.create(order=order, amount=data.get('amount'), status=data.get('status'))
        return Response({'status': 'Payment history created!'})
    
