from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from distancia import views

router = routers.DefaultRouter()
router.register(r'distancia', views.DistanciaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
]