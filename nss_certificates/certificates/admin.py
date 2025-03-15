from django.contrib import admin
from .models import Certificate

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('student', 'approved', 'uploaded_at')
    list_filter = ('approved',)
    actions = ['approve_certificates']

    def approve_certificates(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(Certificate, CertificateAdmin)
