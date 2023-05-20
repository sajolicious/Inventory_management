from django.db import models

# Create your models here.
class stock(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,unique=True,verbose_name="name")
    description = models.CharField(max_length=255, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delated=models.BooleanField(default=False)
    def __str__(self):
        return self.name