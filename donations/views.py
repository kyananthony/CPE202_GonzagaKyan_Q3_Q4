from django.shortcuts import render, get_object_or_404, redirect
from .models import Donor, BloodRequest, Donation

def home(request):
    return render(request,'donations/home.html')

def donor_list(request):
    donors = Donor.objects.all()
    return render(request,'donations/request_list.html',{'requests':requests})

def donate_blood(request, request_id):
    blood_request = get_object_or_404(BloodRequest, id=request_id)
    donor = Donor.objects.get(user=request.user)
    donation = Donation(donor=donor, blood_request=blood_request)
    donation.save()
    return redirect('home')

