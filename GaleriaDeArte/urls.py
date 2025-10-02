from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views as views_core
from album import views as views_album

urlpatterns = [
    path('', views_core.index, name="index"),
    path('album/', views_album.album_list, name="album"),
    path('admin/', admin.site.urls),
    path('info/', views_core.info, name="info"),
    path('preguntas/', views_core.preguntas, name="preguntas"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)