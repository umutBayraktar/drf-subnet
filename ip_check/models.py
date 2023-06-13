from django.db import models

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address
    
class SubIPAddress(models.Model):

    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('DEACTIVE', 'Deactive'),
    )

    ip_address = models.ForeignKey(IPAddress, on_delete=models.PROTECT)
    sub_ip = models.GenericIPAddressField(unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status