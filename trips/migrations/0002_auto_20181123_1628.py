# Generated by Django 2.1.3 on 2018-11-23 16:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import trips.models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='action',
            name='updated_at',
            field=trips.models.AutoDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='media',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='media',
            name='updated_at',
            field=trips.models.AutoDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='place',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='place',
            name='updated_at',
            field=trips.models.AutoDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='trip',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='trip',
            name='updated_at',
            field=trips.models.AutoDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='place',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='trips.Trip'),
        ),
    ]
