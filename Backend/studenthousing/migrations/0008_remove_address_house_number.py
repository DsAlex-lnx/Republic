# Generated by Django 4.1 on 2022-08-31 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studenthousing', '0007_alter_locator_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='house_number',
        ),
    ]
