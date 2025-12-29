# Job Application Tracker
The project is a Job Application Tracker designed to help users manage job applications with CRUD-based REST APIs. It demonstrates backend development, database integration, API consumption, and basic reporting.

## Features
- CRUD operations for job applications
- Third-party API integration for company info
- Reporting API for status summary
- Chart.js visualization of job application statuses

## Tech Stack
- Python 3.12 + Django 6
- PostgreSQL
- Django REST Framework
- Chart.js (frontend)

I attempted deployment on Render, configuring:

gunicorn for production server

Environment variables for database and secret keys

PostgreSQL connection settings

Static file handling for production

However, I encountered runtime issues related to production configuration, particularly:

Static file serving in production

Environment variable inconsistencies

Database connection initialization during build/runtime

Due to the limited timeline, I was unable to fully stabilize the deployment. These issues are deployment-specific and do not affect the local execution of the application.

Current Status

✅ Application fully functional locally

✅ All APIs tested and working

✅ Live Render deployment 
  












