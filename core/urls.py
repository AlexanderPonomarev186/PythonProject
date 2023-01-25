from django.urls import path
from core.views import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'faces'

urlpatterns = [
    path('', views.index,  name='index'),
    path('index', views.index, name='index'),
    path('test', views.test,  name='test'),
    path('api', views.api, name='api'),
    path('statistic', views.statistic, name='statistic')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)