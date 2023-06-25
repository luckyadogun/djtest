from django.urls import path
from .import urls

urlpatterns = [
    path('', urls.index, name='index'),
    path('about/', urls.about, name='about'),
    path('tracking/', urls.tracking, name='tracking'),
    path('support/', urls.support, name='support'),
    path('setup/', urls.setup, name='setup'),
]