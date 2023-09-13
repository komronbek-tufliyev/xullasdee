from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from .views import set_language
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title=_("Sciencelab API"),
        default_version='v1',
        description=_("Sciencelab API description"),
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="komronbek773@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('set_language/<str:language>/', set_language, name='set_language'),
    path('i18n/', include('django.conf.urls.i18n'), name='index'),
    path('set_language/<str:language>/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # prefix_default_language=False,
)

# if settings.DEBUG:
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        # ...
        path('__debug__/', include(debug_toolbar.urls)),
        # ...
    ]

