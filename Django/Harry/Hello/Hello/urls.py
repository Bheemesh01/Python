from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Harry Ice Cream Admin"
admin.site.site_title = "Harry Ice cream portal"
admin.site.index_title = "Welcome to Harry Ice cream Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
