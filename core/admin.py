from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import WebsiteCheck
import csv
from django.http import HttpResponse


@admin.register(WebsiteCheck)
class WebsiteCheckAdmin(admin.ModelAdmin):
    list_display = ('url_colored', 'status_colored', 'ssl_status_colored', 'checked_at_formatted')
    list_filter = ('status_code',)
    search_fields = ('url', 'status_code')
    ordering = ('-checked_at',)
    list_per_page = 20

    # Custom section grouping
    fieldsets = (
        ('Website Information', {'fields': ('url',)}),
        ('Scan Results', {'fields': ('status_code', 'ssl_expiry_days')}),
        ('Timestamps', {'fields': ('checked_at',), 'classes': ('collapse',)}),
    )

    readonly_fields = ('checked_at',)

    # --- Custom Display Methods ---

    def url_colored(self, obj):
        return format_html(
            '<a href="{0}" target="_blank" style="font-weight:600;color:#007bff;text-decoration:none;">{0}</a>', obj.url
        )
    url_colored.short_description = "Website URL"

    def status_colored(self, obj):
        color = "green" if str(obj.status_code).startswith("2") else "red"
        return format_html('<b style="color:{};">{}</b>', color, obj.status_code)
    status_colored.short_description = "HTTP Status"

    def ssl_status_colored(self, obj):
        if obj.ssl_expiry_days is None:
            return format_html('<span style="color:gray;">N/A</span>')
        elif obj.ssl_expiry_days < 0:
            return format_html('<b style="color:red;">Expired</b>')
        elif obj.ssl_expiry_days < 30:
            return format_html('<b style="color:orange;">{} days (⚠️ Expiring Soon)</b>', obj.ssl_expiry_days)
        else:
            return format_html('<b style="color:green;">{} days</b>', obj.ssl_expiry_days)
    ssl_status_colored.short_description = "SSL Expiry"

    def checked_at_formatted(self, obj):
        return obj.checked_at.strftime("%Y-%m-%d %H:%M:%S")
    checked_at_formatted.short_description = "Checked At"

    # --- Export Action ---
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename=WebsiteCheck_{timezone.now().strftime("%Y%m%d_%H%M%S")}.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = [getattr(obj, field) for field in field_names]
            writer.writerow(row)

        return response

    export_as_csv.short_description = "Download selected as CSV"
