from django.contrib import admin
from .models import Donor, BloodRequest, Donation
admin.site.register(Donor)
admin.site.register(BloodRequest)
admin.site.register(Donation)

# Register your models here.
