
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from posts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',views.post_list),
    path('posts/<int:pk>',views.post_detail),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
