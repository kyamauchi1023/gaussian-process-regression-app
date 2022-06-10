from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('gprapp/', include('gprapp.urls'), name="gprapp"),
    path('admin/', admin.site.urls),
]
