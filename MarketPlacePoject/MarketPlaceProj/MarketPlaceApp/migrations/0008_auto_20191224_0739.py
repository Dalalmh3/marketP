# Generated by Django 3.0 on 2019-12-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketPlaceApp', '0007_auto_20191224_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_url',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
