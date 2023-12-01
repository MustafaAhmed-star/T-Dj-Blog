
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from posts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',views.PostList.as_view()),
    path('posts/created/',views.post_create),
    path('posts/delete/<int:pk>/',views.post_delete),
    
    path('posts/create/',views.PostCreate.as_view()),
    path('posts/<int:pk>/',views.PostDetail.as_view()),
    path('posts/edit/<int:pk>/',views.post_edit),
    path('summernote/', include('django_summernote.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
