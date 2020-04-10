"""trial1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard' ),
    path('cg_up/', views.dashboard_vircg, name='dashboard_vircg' ),
    path('vir_dn/', views.dashboard_cgvir, name='dashboard_cgvir' ),
    path('delay_log',views.delay_log, name='delay_log'),
    path('cg_up/<slug:routecode>',views.vircg_route,name='vircg_route'),
    path('cg_up/<slug:routecode>/delay/',views.vircg_delay,name='vircg_delay'),
    path('cg_up/cg_up/<slug:routecode>',views.vircg_route,name='vircg_route'),
    path('cg_up/cg_up/<slug:routecode>/delay/',views.vircg_delay,name='vircg_delay'),
    path('vir_dn/vir_dn/<slug:routecode>',views.cgvir_route,name='cgvir_route'),
    path('vir_dn/vir_dn/<slug:routecode>/delay/',views.cgvir_delay,name='cgvir_delay'),
    path('vir_dn/<slug:routecode>',views.cgvir_route,name='cgvir_route'),
    path('vir_dn/<slug:routecode>/delay/',views.cgvir_delay,name='cgvir_delay'),
    path('station_status/',views.station_status,name="station_status")

]
