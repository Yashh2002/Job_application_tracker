import requests
from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import JobApplication
from .serializers import JobApplicationSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter

class JobApplicationListCreateView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class JobApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class CompanyInfoView(APIView):
    def get(self, request):
        company_name = request.query_params.get('name')

        if not company_name:
            return Response(
                {"error": "Company name is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        domain = company_name.lower().replace(" ", "") + ".com"
        logo_url = f"https://logo.clearbit.com/{domain}"

        return Response(
            {
                "company_name": company_name,
                "logo_url": logo_url
            },
            status=status.HTTP_200_OK
        )

@api_view(['GET'])
def job_status_report(request):
    jobs = JobApplication.objects.all()
    status_list = [job.status for job in jobs]
    status_count = dict(Counter(status_list))

    # Ensure all statuses are included even if zero
    all_statuses = ['Applied', 'Interview', 'Rejected', 'Offer']
    for s in all_statuses:
        if s not in status_count:
            status_count[s] = 0

    return Response(status_count)

def dashboard(request):
    return render(request, 'index.html')
