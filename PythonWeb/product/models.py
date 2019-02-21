from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    timestamp   = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated     = models.DateTimeField(auto_now_add=False, auto_now=True)
    active      = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Product, self).save(*args, **kwargs)