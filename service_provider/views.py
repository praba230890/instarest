import json
from django.http import JsonResponse

from service_creator.models import Endpoint

# Create your views here.
def index(request):
    path = request.path[9:]
    method = request.method
    headers = request.headers
    print(headers)

    endpoint = Endpoint.objects.get(path=path)
    response = json.loads(endpoint.response)
    print(response)
    return JsonResponse(response)