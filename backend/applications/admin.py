from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'job_role',
        'status',
        'applied_date',
        'source',
        'expected_salary',
    )
    list_filter = ('status', 'source')
    search_fields = ('company_name', 'job_role')
