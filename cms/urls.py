"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView,SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    # Swagger Schema URL
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI & Doc URL
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # classes URL
    path('api/',include('classes.urls')),
    # teacher URL
    path('api/',include('teacher.urls')),
    #  student URL
    path('api/',include('student.urls')),
]
