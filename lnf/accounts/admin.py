from django.contrib import admin
from . models import Item,Match,Claim,Report

# Register your models here.

#admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Claim)
admin.site.register(Match)
admin.site.register(Report)
