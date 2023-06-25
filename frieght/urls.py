from django.views import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('tracking/', views.tracking, name='tracking'),
    path('support/', views.support, name='support'),
    path('setup/', views.setup, name='setup'),
]