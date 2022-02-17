from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from posts.models import HealthCheck

def update_counter():
    instance = HealthCheck.objects.first()
    instance.counter += 1
    instance.save()
    print(f"Counter was udated: {instance.counter}")

def check(request):
    data = {"msg": "Server is available"}
    update_counter()
    return JsonResponse(data)
    # return HttpResponse(str(data), content_type="application/json")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health-check/', check),
    path('posts/', include('posts.urls')),
]