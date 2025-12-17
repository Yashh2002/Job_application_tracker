from django.urls import path
from .views import (
    JobApplicationListCreateView,
    JobApplicationDetailView,
    CompanyInfoView,
    job_status_report,
    dashboard
)

urlpatterns = [
    path('jobs/', JobApplicationListCreateView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobApplicationDetailView.as_view(), name='job-detail'),
    path('company-info/', CompanyInfoView.as_view(), name='company-info'),
    path('reports/status-summary/', job_status_report, name='status-report'),
    path('dashboard/', dashboard, name='dashboard'),
]
