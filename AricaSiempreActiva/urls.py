from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
   
    path('gremio/', include('panel_gremio.urls')),
    path('actividades/', views.actividades_publicas, name='actividades_publicas'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)