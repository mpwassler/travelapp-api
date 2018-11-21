# Generated by Django 2.1.3 on 2018-11-17 22:02

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ActionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=560)),
                ('size', models.CharField(max_length=360)),
                ('type', models.CharField(max_length=360)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Entity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip'),
        ),
        migrations.AddField(
            model_name='media',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Place'),
        ),
        migrations.AddField(
            model_name='action',
            name='action_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.ActionType'),
        ),
        migrations.AddField(
            model_name='action',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Entity'),
        ),
    ]
