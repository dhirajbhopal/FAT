# Generated by Django 4.2.5 on 2023-11-18 14:40

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('amount', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='fat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('empid', models.CharField(max_length=15)),
                ('dept', models.CharField(max_length=15)),
                ('circle', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=40)),
                ('grade', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=15)),
                ('certno', models.CharField(max_length=15)),
                ('image', models.ImageField(blank=True, null=True, upload_to=student.models.filepath)),
                ('qr', models.ImageField(blank=True, null=True, upload_to=student.models.filepath)),
                ('status', models.CharField(default='raw', max_length=15, null=True)),
                ('qrlink', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]
