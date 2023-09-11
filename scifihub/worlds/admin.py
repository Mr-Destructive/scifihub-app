from django.contrib import admin

from .models import Character, Location, MagicSystem, Religion, World

admin.site.register(World)
admin.site.register(Character)
admin.site.register(Religion)
admin.site.register(Location)
admin.site.register(MagicSystem)
