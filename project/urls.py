
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from posts import views
from posts import api
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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
    
    
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      
  
 