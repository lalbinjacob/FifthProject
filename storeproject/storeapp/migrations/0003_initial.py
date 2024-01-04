# Generated by Django 5.0 on 2023-12-29 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storeapp', '0002_delete_labproduct_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('birthdate', models.DateField(null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('phone_number', models.PositiveIntegerField(null=True)),
                ('email', models.EmailField(max_length=200)),
                ('address', models.CharField(max_length=250)),
                ('materials_provide', models.CharField(max_length=200, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storeapp.course')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storeapp.department')),
                ('purpose', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storeapp.purpose')),
            ],
        ),
    ]