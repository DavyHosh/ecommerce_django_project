# Generated by Django 5.0.3 on 2024-05-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_shippingaddress_county'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=models.CharField(default='Kenya', max_length=200),
            preserve_default=False,
        ),
    ]
