from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('signup/',views.signup, name='signup'),
    path('',views.user_login, name='signin'),
    path('index/',views.index,name="index"),
    path('logout/',views.user_logout,name='logout'), 
    path('lost_items/',views.lost_items,name="lost_items"),   
    path('found_items/',views.found_items,name="found_items"),
    path('report_lost_items/',views.report_lost_items,name="report_lost_items"),
    path('report_found_items/',views.report_found_items,name="report_found_items"),
    path('claim/',views.claim,name="claim"),
    path('faq/',views.faq,name="faq"),
    path('contact/',views.contact,name="contact"),
    path('success/',views.success, name = 'success')
]
