from django.contrib import admin
from service_creator.models import Service, Endpoint
# Register your models here.

admin.site.register(Service)
admin.site.register(Endpoint)
