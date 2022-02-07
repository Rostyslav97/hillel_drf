from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

def check(request):
    data = {"name": "Rostik"}
    return JsonResponse(data)
    # return HttpResponse(str(data), content_type="application/json")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health-check/', check),
    path('posts/', include('posts.urls')),
]


