# Generated by Django 2.2.4 on 2019-12-18 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketPlaceApp', '0002_auto_20191218_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_url',
            field=models.ImageField(upload_to='../media/'),
        ),
    ]
