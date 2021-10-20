from django.contrib import admin
from .models import MarriageRegister




# Register your models here.
class MarrigeregisterAdmin(admin.ModelAdmin):
  list_display=['id','brideName','groomsName']
admin.site.register(MarriageRegister,MarrigeregisterAdmin)




















