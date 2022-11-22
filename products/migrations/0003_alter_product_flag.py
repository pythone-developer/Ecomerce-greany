# Generated by Django 4.1.3 on 2022-11-11 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_tags_alter_product_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('New', 'New'), ('Feature', 'Feature'), ('Sale', 'Sale')], max_length=10, verbose_name='Flag'),
        ),
    ]