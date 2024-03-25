# Generated by Django 5.0.3 on 2024-03-22 13:27

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(db_default='default_task', max_length=50)),
                ('created_at', models.DateTimeField(db_default=django.db.models.functions.datetime.Now(utc=True))),
                ('completed', models.BooleanField(db_default=False)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
