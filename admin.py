from django.contrib import admin
from .models import *

# Register your models here.

models_list = [Contact, NewUser, ClassesDay, SettingAccount, InvoiceEntry, Firm, accounts, Trainers] 
admin.site.register(models_list)