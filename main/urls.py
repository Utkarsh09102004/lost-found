from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include
from django.conf import settings



urlpatterns = [
    path('register/',views.registration,name='register'),
    path('login/',views.loginPage,name='login'),
    path('',views.home, name='home'),
    path('loser/', views.loser, name='loser'),
    path('founder/', views.founder, name='founder'),
    path('status/',views.status, name='status'),
    path('items/<str:pk>/',views.item,name='item'),
    path('matched/<str:pk>/', views.matched, name='matched'),
    path('contact/<str:pk>/',views.contact,name='contact')

]

from django.conf.urls.static import static

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

