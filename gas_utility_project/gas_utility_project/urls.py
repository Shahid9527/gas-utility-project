# urls.py
from django.contrib import admin
from django.urls import path
from gas_utility.views import (
    submit_service_request, 
    track_request, 
    service_request_list, 
    service_request_detail, 
    update_service_request_status
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/', submit_service_request, name='submit_service_request'),
    path('track/', track_request, name='track_request'),
    path('service-requests/', service_request_list, name='service_request_list'),
    path('service-request/<int:pk>/', service_request_detail, name='service_request_detail'),
    path('service-request/<int:pk>/update-status/', update_service_request_status, name='update_service_request_status'),
]
