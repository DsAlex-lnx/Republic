# Generated by Django 4.1 on 2022-08-17 13:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id_address', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('house_number', models.IntegerField()),
                ('zip_code', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=16)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Republic',
            fields=[
                ('id_republic', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField(max_length=10)),
                ('description', models.CharField(max_length=255)),
                ('house_type', models.IntegerField()),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='studenthousing.address')),
                ('republic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='republics', to='studenthousing.user')),
            ],
        ),
    ]
