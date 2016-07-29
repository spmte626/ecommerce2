from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Product(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    active = models.BooleanField(default=True)
    #inventory?

    def __str__(self):
        return self.title


    def get_absolute_url(self):
    	return reverse("product_detail", kwargs={"pk": self.pk})

# Product Image


# Product Category


