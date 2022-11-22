# Generated by Django 4.1.3 on 2022-11-18 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('type', models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Academy', 'Academy'), ('Others', 'Others')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_phone', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Academy', 'Academy'), ('Others', 'Others')], max_length=10)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=80)),
                ('notes', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_adress', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='users')),
                ('code', models.CharField(default='54907136', max_length=10)),
                ('code_used', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]