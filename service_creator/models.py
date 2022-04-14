from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)

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

    def __str__(self):
        return self.name + " : " + self.path
    
    def __repr__(self):
        return self.name + " : " + self.path