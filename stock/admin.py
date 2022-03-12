from django.contrib import admin
from .models import stock, RegistrationFormDemant, fund
# Register your models here.
admin.site.register(stock)
admin.site.register(RegistrationFormDemant)
admin.site.register(fund)