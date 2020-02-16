from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    advertiser = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.CharField(max_length=200, default='')
    item = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.item



