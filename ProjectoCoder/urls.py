
from django.contrib import admin
from django.urls import path, include
from AppCoder import urls
from AppCoder.views import curso
urlpatterns = [

    path('admin/', admin.site.urls),
    path('curso/', curso),
    path('AppCoder/' , include('AppCoder.urls')),
]
