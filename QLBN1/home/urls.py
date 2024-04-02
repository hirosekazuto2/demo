from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path('', views.queue,name='queue'),
    path('create/',views.patient_create,name='patient_create'),
    path("",views.patient_list, name="patient_list"),
    #path('update/',views.patient_update,name='patient_update'),
    path('update/str:idP>/',views.patient_update,name='patient_update')
]