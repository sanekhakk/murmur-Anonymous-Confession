from django.contrib import admin
from django.urls import path, include
from core import views  # replace 'core' with your app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', views.home, name='home'),
    path('post/', views.post_confession, name='post_confession'),
]
