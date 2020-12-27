from django.db import models

# Create your models here.

class GetInfo(models.Model):
    ResponseCode = models.CharField(max_length=100, blank=True, null=True , default='')
    PortalOneSessionKey = models.CharField(max_length=100, blank=True, null=False)
    ResponseMessage = models.CharField(max_length=100, blank=True, null=True)
    ExternalCustomerId = models.CharField(max_length=100, blank=True, null=True)
    CustomerName = models.CharField(max_length=100, blank=True, null=True)
    CustomerId	= models.CharField(max_length=100, blank=True, null=True, default='')

    def __str__(self):
        return self.PortalOneSessionKey