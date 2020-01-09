from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Volunteer
from django.contrib.auth.models import User
from django.utils import timezone
# Create your views here.
def create(request):
    if request.method == 'POST':
            if request.POST['Name'] and request.POST['Age']  and request.POST['Campaign_id']  and request.POST['Email']  and request.POST['PhoneNumber']  and request.POST['Country']  and request.POST['State']  and request.POST['City']  :
                volunteer = Volunteer()
                volunteer.Name = request.POST['Name']
                volunteer.Age = request.POST['Age']
                volunteer.Campaign_id = request.POST['Campaign_id']
                volunteer.PhoneNumber = request.POST['PhoneNumber']
                volunteer.Country = request.POST['Country']
                volunteer.State = request.POST['State']
                volunteer.City = request.POST['City']
                volunteer.save()

                return redirect('/thanku/')
            else:
                return render(request, 'volunteer/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'volunteer/create.html')
