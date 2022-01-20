from django.http import JsonResponse

def posts(request):
    return JsonResponse({"results": []})