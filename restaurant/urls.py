"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from rest.views import main_page, booking_table, email_confirmation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main'),
    # path('booking_table/<pk>', booking_table, name='booking_table'),
    path('booking_table/', booking_table, name='booking_table'),
    path('confirm/<pk>', email_confirmation, name='email')
]
