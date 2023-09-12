from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('botuser', BotUserViewSet)
router.register('comment', CommentViewSet)
router.register('order', OrderViewSet)
router.register('category', CategoryViewSet)
router.register('subcategory', SubCategoryViewSet)
router.register('orderhistory', OrderHistoryViewSet)
router.register('orderfile', OrderFileViewSet)


urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('api/change_language/', ChangeLanguage.as_view(), name='change_language'),
    path('api/change-phone/', ChangePhoneNumber.as_view(), name='change_phone'),
    path('api/generate-fake-data/', generate_data, name='generate_data'),   
]