from django.contrib.admin import ModelAdmin, register, TabularInline
from .models import Lead

@register(Lead)
class LeadAdmin(ModelAdmin):
    pass