from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('botusers', BotUserViewSet)
router.register('comments', CommentViewSet)
router.register('orders', OrderViewSet)
router.register('categories', CategoryViewSet)
router.register('subcategories', SubCategoryViewSet)
router.register('orderhistories', OrderHistoryViewSet)
router.register('orderfiles', OrderFileViewSet)


urlpatterns = [
    # This will be the main page
    path('', index, name='index'),

    path('api/', include(router.urls)),
    
    # Auth endpoints. POST methods
    path('api/change_language/', ChangeLanguage.as_view(), name='change_language'),
    path('api/change-phone/', ChangePhoneNumber.as_view(), name='change_phone'),
    # POST method. Generate fake data
    path('api/generate-fake-data/', generate_data, name='generate_data'),

    # Main endpoints

    # POST methods
    path('api/payment/', PaymentView.as_view(), name='payment'),
    path('api/set-order/', SetOrderView.as_view(), name='set_order'),
    path('api/change-order-status/', ChangeOrderStatusView.as_view(), name='change_order'),
    path('api/change-order-item/', ChangeOrderItemView.as_view(), name='change_order_item'),
    path('api/change-order-files/', ChangeOrderFilesView.as_view(), name='change_order_files'),
    path('api/set-order-history/', SetOrderHistoryView.as_view(), name='set_order_history'),

    # GET methods
    path('api/my-orders/', MyOrdersView.as_view(), name='my_orders'),
    path('api/order-status/', CheckOrderStatusView.as_view(), name='order_status'),
    path('api/get-files/', GetOrderFilesView.as_view(), name='get_files'),
    path('api/order-history/', GetOrderHistoryView.as_view(), name='order_history'),   

    # DELETE methods
    path('api/delete-order/', DeleteOrderView.as_view(), name='delete_order'),
]

