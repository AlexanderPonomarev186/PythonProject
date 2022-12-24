from django.contrib import admin
from core.models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "year", "cost",)
    list_display_links = ("pk", "name", "year", "cost",)
    readonly_fields = ('pk',)