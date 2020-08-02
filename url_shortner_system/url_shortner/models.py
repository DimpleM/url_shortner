from __future__ import unicode_literals
from django.db import models

# Create your models here.
class URLs(models.Model):
	expiry_time = models.DateTimeField(null=True, blank=True)
	shortURL = models.CharField(max_length=8,primary_key=True)
	targetURL = models.CharField(max_length=2083)
	created = models.DateTimeField(auto_now_add=True, blank=True)
	private_token = models.CharField(blank=True,max_length=200)
	click_info = models.IntegerField(default=1)

