from django.contrib import admin
from .models import SystemParam


@admin.register(SystemParam)
class SystemParamAdmin(admin.ModelAdmin):
    search_fields = ("name", "value")
    list_display = ("name", "value", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    show_full_result_count = False
