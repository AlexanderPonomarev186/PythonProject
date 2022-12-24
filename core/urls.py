from django.urls import path
from core.views import views

app_name = 'faces'

urlpatterns = [
    path('', views.index,  name='index'),
    path('test', views.test,  name='test')
]