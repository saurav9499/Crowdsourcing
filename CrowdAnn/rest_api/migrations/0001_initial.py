# Generated by Django 3.0.4 on 2020-03-24 12:58

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('image_source', models.URLField()),
                ('provider_id', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('annotation_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('user', models.IntegerField()),
                ('coordinates', django.contrib.gis.db.models.fields.PolygonField(null=True, srid=4326)),
                ('label', models.CharField(max_length=300)),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.Image')),
            ],
        ),
    ]
