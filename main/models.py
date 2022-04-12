from django.db import models
from django.urls import reverse


# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='new', null=True, blank=True)
    description = models.CharField(max_length=100)
    new_price = models.IntegerField(max_length=30 , null=True, blank=True)
    off_price = models.IntegerField(max_length=30, null=True, blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        # filename = self.image.url

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    is_trending = models.BooleanField(default=False)


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Company(models.Model):
    company_name = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name