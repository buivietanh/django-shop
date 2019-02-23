from django.db import models
from django.utils.text import slugify
from django.urls import reverse

def upload_location(instance, filename):
    return '%s/%s' %(instance.id, filename)

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    thumbnail   = models.FileField(upload_to='thumbnails/', null=True, blank=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sale_price  = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated     = models.DateTimeField(auto_now_add=False, auto_now=True)
    active      = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    class Meta:
        unique_together = ('title', 'slug')
    
    def get_absolute_url(self):
        #return '/product/%s' %(self.slug)
        return reverse('single_product', kwargs={'slug': self.slug})
        #return reverse('single_product', args={self.slug})
    

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Product, self).save(*args, **kwargs)

class ProductImage(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    aaaffff     = models.CharField(max_length=120, null=True)
    image       = models.ImageField(upload_to=upload_location, null=True)
    featured    = models.BooleanField(default=False)
    updated     = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.title
    