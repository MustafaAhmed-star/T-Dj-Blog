
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from posts import views
from posts import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',views.PostList.as_view()),
    path('posts/created/',views.post_create),
    path('posts/edit/<int:pk>/',views.post_edit),
    path('posts/deleted/<int:pk>/',views.post_delete), 
    
    path('api-auth/', include('rest_framework.urls')),
    
    path('posts/create/',views.PostCreate.as_view()),
    path('posts/<int:pk>/',views.PostDetail.as_view()),
    
    path('posts/delete/<int:pk>/',views.PostDelete.as_view()),
    path('summernote/', include('django_summernote.urls')),
   # path('posts/api/',api.postListApi),
    path('posts/api/',api.PostListApi.as_view()),
    path('posts/api/<int:pk>/',api.PostDetailApi.as_view()),
    path('posts/api/RUD/<int:pk>/',api.PostRUDapi.as_view()),
    #path('posts/api/<int:pk>/',api.postDetailApi),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
