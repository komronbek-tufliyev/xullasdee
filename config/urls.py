from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from .views import set_language

urlpatterns = [
    path('set_language/<str:language>/', set_language, name='set_language'),
    path('i18n/', include('django.conf.urls.i18n'), name='index'),
]

urlpatterns += i18n_patterns(
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('set_language/<str:language>/', set_language, name='set_language'),
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

