# Generated by Django 5.1.7 on 2025-03-19 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('section_office', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('worker_id', models.BigIntegerField(blank=True, null=True)),
                ('section_Office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='section_office.officedetails')),
            ],
        ),
    ]
