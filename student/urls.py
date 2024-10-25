from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('insert', views.insert),
    path('empfatdata', views.empfatdata),
    path('upload', views.upload),
    path('insertqr', views.insertqr),
    path('newphoto', views.newphoto),
    path('updatephoto', views.updatephoto),
    path('editdata', views.editdata),
    path('edit', views.edit),
    path('all', views.all),
    path('', views.logins),
    path('updateqr', views.updateqr),
    path('printfat', views.printfat),
    path('donate', views.donate),
    path('donationdetail', views.donationdetail),
    path('login', views.logintask),
    path('logout_view', views.logout_view),
   ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
