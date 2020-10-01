# Generated by Django 3.0.8 on 2020-10-01 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email address')),
                ('contact', models.CharField(max_length=15, unique=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='UserProfileData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40)),
                ('company_name', models.CharField(blank=True, max_length=40)),
                ('age', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_data',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=40)),
                ('city', models.CharField(blank=True, max_length=40)),
                ('state', models.CharField(blank=True, max_length=40)),
                ('pin_code', models.CharField(blank=True, max_length=40)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='profile_api.UserProfileData')),
            ],
            options={
                'db_table': 'user_address',
            },
        ),
    ]