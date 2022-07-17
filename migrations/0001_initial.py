# Generated by Django 3.0.5 on 2022-07-03 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_name', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('mobile', models.IntegerField(default='')),
                ('user_type', models.CharField(default='Customer', max_length=150, verbose_name='user_type')),
                ('trainer_name', models.CharField(blank=True, max_length=150, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_membership', models.CharField(blank=True, max_length=150)),
                ('account_camount', models.IntegerField(default='0')),
                ('account_tamount', models.IntegerField(default='0')),
                ('next_pay_date_cust', models.DateField(blank=True, null=True)),
                ('next_pay_date_trainer', models.DateField(blank=True, null=True)),
                ('NewUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_fname', models.CharField(default='', max_length=50)),
                ('contact_mobile', models.IntegerField(default='')),
                ('contact_email', models.CharField(default='', max_length=30)),
                ('contact_club', models.CharField(default='', max_length=1000)),
                ('contact_message', models.CharField(default='', max_length=1000)),
                ('contact_status', models.CharField(default='New', max_length=20)),
                ('contact_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerEmail', models.EmailField(max_length=254, verbose_name='email address')),
                ('ownerMobile', models.IntegerField(default='')),
                ('companyLogo', models.ImageField(upload_to='ecom')),
                ('company', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SettingAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SettingAccount_days', models.IntegerField(default='')),
                ('SettingAccount_month', models.IntegerField(default='')),
                ('SettingAccount_year', models.IntegerField(default='')),
                ('SettingAccount_daysAmt', models.IntegerField(default='')),
                ('SettingAccount_monthAmt', models.IntegerField(default='')),
                ('SettingAccount_yearAmt', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(default='AdminTrainer', max_length=50)),
                ('trainer_email', models.EmailField(default='AdminTrainer@gmail.com', max_length=254, unique=True, verbose_name='email address')),
                ('trainer_mobile', models.IntegerField(blank=True, null=True)),
                ('NewUser', models.ForeignKey(blank=True, limit_choices_to={'is_active': True, 'is_superuser': False}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_membership', models.CharField(blank=True, max_length=150)),
                ('invoice_camount', models.IntegerField(default='')),
                ('invoice_tamount', models.IntegerField(default='')),
                ('NewUser', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('accounts', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='trainingWebsites.accounts')),
            ],
        ),
        migrations.CreateModel(
            name='ClassesDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassesDay_Mon', models.CharField(default='', max_length=50)),
                ('ClassesDay_Mon_class', models.CharField(default='', max_length=500)),
                ('ClassesDay_Tue', models.CharField(default='', max_length=50)),
                ('ClassesDay_Tue_class', models.CharField(default='', max_length=500)),
                ('ClassesDay_Wed', models.CharField(default='', max_length=50)),
                ('ClassesDay_Wed_class', models.CharField(default='', max_length=500)),
                ('ClassesDay_Thru', models.CharField(default='', max_length=50)),
                ('ClassesDay_Thru_class', models.CharField(default='', max_length=500)),
                ('ClassesDay_Fri', models.CharField(default='', max_length=50)),
                ('ClassesDay_Fri_class', models.CharField(default='', max_length=500)),
                ('ClassesDay_Sat', models.CharField(default='', max_length=50)),
                ('ClassesDay_Sat_class', models.CharField(default='', max_length=500)),
                ('ClassesDay_Sun', models.CharField(default='', max_length=50)),
                ('ClassesDay_Sun_class', models.CharField(default='', max_length=500)),
                ('ClassMessage', models.CharField(default='', max_length=500)),
                ('NewUser', models.ForeignKey(limit_choices_to={'is_active': True, 'is_superuser': False, 'user_type': 'Customer'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Trainers', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='trainingWebsites.Trainers')),
            ],
        ),
    ]
