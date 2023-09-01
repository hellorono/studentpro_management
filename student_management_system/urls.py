
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,Staff_views,Hod_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    path('index',views.Index,name='index'),


    path('',views.loginuser,name='login'),
    path('dologin',views.dologin,name='dologin'),

    path('Hod/Home',Hod_views.HOME,name='home'),





]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
