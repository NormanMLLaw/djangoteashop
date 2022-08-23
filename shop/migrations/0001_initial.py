# Generated by Django 3.2.14 on 2022-08-23 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tea_name', models.CharField(max_length=100, unique=True)),
                ('tea_type', models.CharField(max_length=100)),
                ('color', models.CharField(blank=True, max_length=50)),
                ('aroma', models.TextField(blank=True, max_length=100)),
                ('taste', models.TextField(blank=True, max_length=100)),
                ('tea_nature', models.TextField(blank=True, max_length=200)),
                ('properties', models.TextField(blank=True, max_length=200)),
                ('package', models.TextField(blank=True, max_length=200)),
                ('size', models.CharField(blank=True, max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('is_new', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('store', models.IntegerField()),
                ('image', models.ImageField(upload_to='photos/products')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('stars', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
