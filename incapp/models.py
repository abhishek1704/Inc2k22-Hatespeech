from django.db import models

# Create your models here.
class Result(models.Model):
    sent_text = models.CharField(blank=True, null=True, max_length=500)
    hate_label = models.FloatField(blank=True, null=False)
    offn_label = models.FloatField(blank=True, null=False)
    prfn_label = models.FloatField(blank=True, null=False)
    not_label = models.FloatField(blank=True, null=False)
