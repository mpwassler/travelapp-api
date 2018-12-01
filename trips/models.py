from django.contrib.gis.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.datetime.now()

# Create your models here.
class Entity(models.Model):
	pass

class Trip(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
	created_at = models.DateField(default=timezone.now)
	updated_at = AutoDateTimeField(default=timezone.now)

class Place(models.Model):
	label = models.TextField()
	date = models.DateTimeField()
	location = models.PointField()
	trip = models.ForeignKey(Trip, related_name='places', on_delete=models.CASCADE)
	created_at = models.DateField(default=timezone.now)
	updated_at = AutoDateTimeField(default=timezone.now)

class Media(models.Model):
	url = models.CharField(max_length=560)
	size = models.CharField(max_length=360)
	type = models.CharField(max_length=360)
	entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
	place = models.ForeignKey(Place, on_delete=models.CASCADE)
	created_at = models.DateField(default=timezone.now)
	updated_at = AutoDateTimeField(default=timezone.now)

class ActionType(models.Model):
	name = models.CharField(max_length=200)

class Action(models.Model):
	entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
	action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateField(default=timezone.now)
	updated_at = AutoDateTimeField(default=timezone.now)


def create_entity_id(sender, instance, **kwargs):
	print(vars(instance))
	if not instance.entity_id:
		entity = Entity.objects.create()
		instance.entity_id = entity.pk

models.signals.pre_save.connect(create_entity_id, sender=Trip)
models.signals.pre_save.connect(create_entity_id, sender=Media)
