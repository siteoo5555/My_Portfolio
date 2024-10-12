"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from App.views import *   
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
    path('about/', about, name='about'),
    path('portfolio-details/', portfolio_details, name='portfolio_details'),
    path('portfolio/', portfolio, name='portfolio'),
    path('service-details/', service_details, name='service_details'),
    path('services/', services, name='services'),
    path('starter/', starter_page, name='starter_page'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
