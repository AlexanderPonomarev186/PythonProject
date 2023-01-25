from django.contrib import admin
from core.models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "year", "cost")
    list_display_links = ("pk", "name", "year", "cost")
    readonly_fields = ('pk',)


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("pk", "description", "image")
    list_display_links = ("pk",)
    readonly_fields = ('pk',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("pk", "name","image",)
    list_display_links = ("pk","name",)
    readonly_fields = ('pk',)

