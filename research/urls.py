from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from research import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('blog.urls',namespace="blog")),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
