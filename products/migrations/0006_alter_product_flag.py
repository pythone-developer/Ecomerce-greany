# Generated by Django 4.1.3 on 2022-11-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_flag_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('New', 'New'), ('Sale', 'Sale'), ('Feature', 'Feature')], max_length=10, verbose_name='Flag'),
        ),
    ]
