from django.contrib import admin
from .models import MalibuModel, GentraModel, CobaltModel, NexiaModel 

# Register your models here.

@admin.register(MalibuModel)
class MalibuModelAdmin(admin.ModelAdmin):
    pass

@admin.register(GentraModel)
class GentraModelAdmin(admin.ModelAdmin):
    pass

@admin.register(CobaltModel)
class CobaltModelAdmin(admin.ModelAdmin):
    pass

@admin.register(NexiaModel)
class NexiaModelAdmin(admin.ModelAdmin):
    pass