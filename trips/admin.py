from django.contrib import admin

# Register your models here.
from .models import Entity, Trip, ActionType, Action, Place
# Register your models here.

admin.site.register(Entity)
admin.site.register(Trip)
admin.site.register(ActionType)
admin.site.register(Action)
admin.site.register(Place)
