import re
import hashlib

from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    service_identifier = models.CharField(max_length=30, unique=True)

    def save(self, *args, **kwargs):
        hash_object = hashlib.sha1(self.name.encode('utf-8'))
        try:
            self.service_identifier = str(Service.objects.latest('id').id+1)
        except:
            self.service_identifier = str(1)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Endpoint(models.Model):
    name = models.CharField(max_length=30)
    # path should be a valid URL and need to update the length(needs analysis)
    path = models.CharField(max_length=225)
    # the request and response needs to be udpated with json type
    request = models.TextField()
    response = models.TextField()
    headers = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    validate_request = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.request = re.sub(r'(\s|\u180B|\u200B|\u200C|\u200D|\u2060|\uFEFF)+', '', self.request)
        self.response = re.sub(r'(\s|\u180B|\u200B|\u200C|\u200D|\u2060|\uFEFF)+', '', self.response)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + " : " + self.path
    
    def __repr__(self):
        return self.name + " : " + self.path