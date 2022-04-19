from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='new', null=True, blank=True)
    description = models.CharField(max_length=100)
    new_price = models.IntegerField(null=True, blank=True)
    off_price = models.IntegerField(null=True, blank=True)
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


class ProductDescription(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    product_specification = models.TextField(max_length=200)

    desc_name_1 = models.CharField(max_length=50)
    desc_image_1 = models.ImageField(upload_to='new', null=True, blank=True)
    desc_detail_1 = models.TextField()

    desc_name_2 = models.CharField(max_length=50, null=True, blank=True)
    desc_image_2 = models.ImageField(upload_to='new', null=True, blank=True)
    desc_detail_2 = models.TextField(null=True, blank=True)

    desc_name_3 = models.CharField(max_length=50, null=True, blank=True)
    desc_image_3 = models.ImageField(upload_to='new', null=True, blank=True)
    desc_detail_3 = models.TextField(null=True, blank=True)

    desc_name_4 = models.CharField(max_length=50, null=True, blank=True)
    desc_image_4 = models.ImageField(upload_to='new', null=True, blank=True)
    desc_detail_4 = models.TextField(null=True, blank=True)

    desc_name_5 = models.CharField(max_length=50, null=True, blank=True)
    desc_image_5 = models.ImageField(upload_to='new', null=True, blank=True)
    desc_detail_5 = models.TextField(null=True, blank=True)


class AdditionalInfo(models.Model):
    product = models.ForeignKey(
        'Product',
        related_name='product1',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    product_2 = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    capacity_1 = models.CharField(max_length=50)
    weight_dimension_1 = models.TextField()
    display_1 = models.TextField()
    chip_1 = models.TextField()
    isight_cam1 = models.TextField()
    video_record1 = models.TextField()

    capacity_2 = models.CharField(max_length=50)
    weight_dimension_2 = models.TextField()
    display_2 = models.TextField()
    chip_2 = models.TextField()
    isight_cam2 = models.TextField()
    video_record2 = models.TextField(null=True, blank=True)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["not_required"].required = False


class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )

    # product foreign key
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        null= True, blank=True
    )
    review = models.TextField()
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),

    )
    rating = models.IntegerField(choices=RATING_CHOICES , null=True, blank= True)
