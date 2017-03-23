from django.shortcuts import render,redirect
from app.forms import PersonInfoForm
from app.models import PersonInfo
from django.http import HttpResponse

def index(request):
	return HttpResponse("WELCOME TO STUDENT INFORMATION SYSTEM")


def base(request):
    if request.method == "POST":
        form = PersonInfoForm(request.POST)
        if form.is_valid():
            PersonInfo = form.save(commit=False)
            PersonInfo.save()
            return redirect('success')
    else:
        form = PersonInfoForm()
    return render(request, 'app/base.html', {'form': form})
def success(request):
	return HttpResponse("Successfully updated")

