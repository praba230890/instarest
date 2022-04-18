import json
from django.http import JsonResponse

from service_creator.models import Endpoint

# Create your views here.
def index(request):
    path = request.path[9:]
    service_identifier = path.split('/')[1]
    path = "/"+"/".join(path.split('/')[2:])
    print(path, service_identifier)
    method = request.method
    # headers = request.headers

    if request.META.get('CONTENT_TYPE') != "application/json":
        return JsonResponse({"error": "Content-Type must be application/json"})

    request_body = json.loads(request.body)
    endpoint = Endpoint.objects.get(path=path, service__service_identifier=service_identifier)
    endpoint_response = json.loads(endpoint.response)
    if is_valid_request(request_body, endpoint):
        return JsonResponse(endpoint_response)
    return JsonResponse({"error": "No data found for this request"})

def is_valid_request(request_body, endpoint):
    return (not endpoint.validate_request or (endpoint.validate_request and request_body == json.loads(endpoint.request)))