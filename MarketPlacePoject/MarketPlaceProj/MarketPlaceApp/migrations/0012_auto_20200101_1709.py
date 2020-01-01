# Generated by Django 3.0 on 2020-01-01 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MarketPlaceApp', '0011_remove_product_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pName',
            new_name='Product_Name_En',
        ),
        migrations.AddField(
            model_name='product',
            name='Product_Name_Ar',
            field=models.CharField(default=django.utils.timezone.now, max_length=45),
            preserve_default=False,
        ),
    ]
