from django.db import models

# Create your models here.

class GetInfo(models.Model):
    responseCode = models.CharField(max_length=100)
    portalOneSessionKey = models.CharField(max_length=100)

    def __str__(self):
        return self.responseCode