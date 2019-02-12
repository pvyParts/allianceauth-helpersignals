from django.db import models
from allianceauth.eveonline.models import EveCorporationInfo

class ApplicationWebhook(models.Model):
    corp = models.ForeignKey(EveCorporationInfo, on_delete=models.CASCADE)
    enabled = models.BooleanField()
    webhook = models.TextField()

