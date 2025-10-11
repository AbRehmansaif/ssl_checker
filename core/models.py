from django.db import models


class WebsiteCheck(models.Model):
    url = models.URLField()
    status_code = models.CharField(max_length=10)
    ssl_expiry_days = models.IntegerField(null=True)
    checked_at = models.DateTimeField(auto_now_add=True)