from django.shortcuts import render
from faculty.forms import DetailsForm
from faculty.models import Details
from django.http import HttpResponse


#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def index(request):
	return HttpResponse("hello!!!!!!!!")
def base(request):
    if request.method == "POST":
        form = DetailsForm(request.POST)
        if form.is_valid():
            Details = form.save(commit=False)
            Details.save()
            return redirect('success')
    else:
        form = DetailsForm()
    return render(request, 'apps/base.html', {'form': form})
def success(request):
	return HttpResponse("Successfully updated")


