

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('',views.page1,name='home'),
    path('work/',views.work_images,name='work')
         
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
