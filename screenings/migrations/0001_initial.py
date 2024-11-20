# Generated by Django 5.1.3 on 2024-11-19 14:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.IntegerField(default=299)),
                ('carriage', models.IntegerField()),
                ('poezd_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trains.train')),
            ],
        ),
    ]