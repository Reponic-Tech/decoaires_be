# Generated by Django 2.1 on 2018-08-16 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decoaire_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cloth_type',
            field=models.CharField(default='cotton', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_ppal',
            field=models.FileField(default=0, upload_to='product_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
