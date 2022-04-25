from django.contrib import admin
from .models import Boat, FAO_Zone, Fish_Species, Fish_Catch, Catch_Composition

admin.site.register(Boat)
admin.site.register(FAO_Zone)
admin.site.register(Fish_Species)
admin.site.register(Fish_Catch)
admin.site.register(Catch_Composition)
