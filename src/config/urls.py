from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('health-check/', check),
    path('posts/', include('posts.urls')),
]
