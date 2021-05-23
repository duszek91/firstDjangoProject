from django.contrib import admin
from .models import Calculation
# Register your models here.

@admin.register(Calculation)
class CalculationAdmin(admin.ModelAdmin):
    list_display = ['operation', 'arg_a', 'arg_b', 'result']
    list_filter = ['operation']

