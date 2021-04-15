from django.contrib import admin
from . models import Tweet, Contact,  Category
# Register your models here.
admin.site.register(Tweet)
admin.site.register(Contact)
admin.site.register(Category)