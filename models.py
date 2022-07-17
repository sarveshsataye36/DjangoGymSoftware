from pyexpat import model
from statistics import mode
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField
    contact_fname = models.CharField(max_length=50,default="")
    contact_mobile = models.IntegerField(default="")
    contact_email = models.CharField(max_length=30,default="")
    contact_club = models.CharField(max_length=1000,default="")
    contact_message = models.CharField(max_length=1000,default="")
    contact_status = models.CharField(max_length=20,default="New")
    contact_date = models.DateField()

    def __str__(self):
        return self.contact_email

#custom user model start here
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, mobile, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('user_type', 'Customer')
        other_fields.setdefault('trainer_name', '')

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, mobile, password, **other_fields)

    def create_user(self, email, user_name, first_name,mobile, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name,mobile=mobile, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateField(auto_now_add=True)
    mobile = models.IntegerField(default="")
    user_type = models.CharField(_('user_type'),max_length=150,default="Customer")
    trainer_name = models.CharField(max_length=150, blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name','mobile']

    def __str__(self):
        return self.user_name

#custom user model end here
class accounts(models.Model):
    NewUser = models.ForeignKey("NewUser",on_delete=models.CASCADE)
    account_id = models.AutoField
    account_membership = models.CharField(max_length=150, blank=True)
    account_camount = models.IntegerField(default="0")
    account_tamount = models.IntegerField(default="0")
    next_pay_date_cust = models.DateField(null=True,blank=True)
    next_pay_date_trainer = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.NewUser.first_name

class Firm(models.Model):
    ownerEmail = models.EmailField(_('email address'))
    ownerMobile = models.IntegerField(default="")
    companyLogo = models.ImageField(upload_to='ecom')
    company = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.company

class InvoiceEntry(models.Model):
    NewUser = models.ForeignKey("NewUser",on_delete=models.CASCADE,default="")
    accounts = models.ForeignKey("accounts",on_delete=models.CASCADE,default="")
    invoice_membership = models.CharField(max_length=150, blank=True)
    invoice_camount = models.IntegerField(default="")
    invoice_tamount = models.IntegerField(default="")
    def __str__(self):
        return self.invoice_membership

class SettingAccount(models.Model):
    SettingAccount_days = models.IntegerField(default="")
    SettingAccount_month = models.IntegerField(default="")
    SettingAccount_year = models.IntegerField(default="")
    SettingAccount_daysAmt = models.IntegerField(default="")
    SettingAccount_monthAmt = models.IntegerField(default="")
    SettingAccount_yearAmt = models.IntegerField(default="")

class Trainers(models.Model):
    NewUser = models.ForeignKey("NewUser",on_delete=models.CASCADE,limit_choices_to={'is_superuser':False,'is_active':True},null = True,blank = True)
    trainer_name = models.CharField(max_length=50,default="AdminTrainer")
    trainer_email = models.EmailField(_('email address'), unique=True,default="AdminTrainer@gmail.com")
    trainer_mobile = models.IntegerField(null = True,blank = True)
    def __str__(self):
        return self.trainer_name

class ClassesDay(models.Model):
    NewUser = models.ForeignKey("NewUser",on_delete=models.CASCADE,limit_choices_to={'user_type':'Customer','is_superuser':False,'is_active':True})
    Trainers = models.ForeignKey("Trainers",on_delete=models.CASCADE,default="")
    ClassesDay_id = models.AutoField
    ClassesDay_Mon = models.CharField(max_length=50,default="")
    ClassesDay_Mon_class = models.CharField(max_length=500,default="")
    ClassesDay_Tue = models.CharField(max_length=50,default="")
    ClassesDay_Tue_class = models.CharField(max_length=500,default="")
    ClassesDay_Wed = models.CharField(max_length=50,default="")
    ClassesDay_Wed_class = models.CharField(max_length=500,default="")
    ClassesDay_Thru = models.CharField(max_length=50,default="")
    ClassesDay_Thru_class = models.CharField(max_length=500,default="")
    ClassesDay_Fri = models.CharField(max_length=50,default="")
    ClassesDay_Fri_class = models.CharField(max_length=500,default="")
    ClassesDay_Sat = models.CharField(max_length=50,default="")
    ClassesDay_Sat_class = models.CharField(max_length=500,default="")
    ClassesDay_Sun = models.CharField(max_length=50,default="")
    ClassesDay_Sun_class = models.CharField(max_length=500,default="")
    ClassMessage = models.CharField(max_length=500,default="")
    def __str__(self):
        return self.NewUser.first_name