"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

