# Generated by Django 4.0.4 on 2022-05-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendencesystem', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
