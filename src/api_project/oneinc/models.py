from django.db import models

# Create your models here.

class GetInfo(models.Model):
    ResponseCode = models.CharField(max_length=100, default='')
    PortalOneSessionKey = models.CharField(max_length=100)
    ResponseMessage = models.CharField(max_length=100)

    def __str__(self):
        return self.ResponseCode