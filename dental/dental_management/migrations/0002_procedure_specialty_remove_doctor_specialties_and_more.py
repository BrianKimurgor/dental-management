# Generated by Django 5.1.4 on 2024-12-07 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dental_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='specialties',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='procedures',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='procedure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental_management.procedure'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(to='dental_management.specialty'),
        ),
        migrations.AddField(
            model_name='visit',
            name='procedures',
            field=models.ManyToManyField(to='dental_management.procedure'),
        ),
    ]
