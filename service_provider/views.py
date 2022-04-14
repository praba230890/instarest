import json
from django.http import JsonResponse

from service_creator.models import Endpoint

# Create your views here.
def index(request):
    path = request.path[9:]
    method = request.method
    # headers = request.headers

    if request.META.get('CONTENT_TYPE') != "application/json":
        return JsonResponse({"error": "Content-Type must be application/json"})

    req_body = json.loads(request.body)
    endpoint = Endpoint.objects.get(path=path)
    endpoint_body = json.loads(endpoint.request)
    response = json.loads(endpoint.response)
    if req_body == endpoint_body:
        return JsonResponse(response)
    return JsonResponse({"error": "No data found for this request"})
