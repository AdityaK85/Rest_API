# Generated by Django 4.2.3 on 2023-07-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]