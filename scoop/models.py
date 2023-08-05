from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            viewname='sale_detail',
            kwargs={
                "pk": self.pk
            }
        )
    
    class Meta:
        ordering = ['-id']


class RepairProduct(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='repairs/%Y/%m/%d/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
