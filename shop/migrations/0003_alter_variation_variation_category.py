# Generated by Django 3.2.14 on 2022-09-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('size', 'size'), ('package', 'package')], max_length=100),
        ),
    ]
