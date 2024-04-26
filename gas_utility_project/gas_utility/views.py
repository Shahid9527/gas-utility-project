from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'gas_utility/submit_request.html', {'form': form})

@login_required
def track_request(request):
    user_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'gas_utility/track_request.html', {'user_requests': user_requests})

@login_required
def service_request_list(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'gas_utility/service_request_list.html', {'service_requests': service_requests})

@login_required
def service_request_detail(request, pk):
    service_request = ServiceRequest.objects.get(pk=pk)
    return render(request, 'gas_utility/service_request_detail.html', {'service_request': service_request})

@login_required
def update_service_request_status(request, pk):
    service_request = ServiceRequest.objects.get(pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        service_request.status = new_status
        service_request.save()
        return redirect('service_request_detail', pk=pk)
    return render(request, 'gas_utility/update_service_request_status.html', {'service_request': service_request})
