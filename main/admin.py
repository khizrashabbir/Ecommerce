from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductDescription)
admin.site.register(AdditionalInfo)
admin.site.register(Review)
