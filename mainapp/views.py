from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import View

from .models import Maintenance
from .models import AnnualReport
from django.http import JsonResponse
from mainapp.Forms import MainForm
from mainapp.Forms import annualrepForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#def home(request):
#	return render(request, 'mainapp/index.html')

@login_required
def home(request):
	maintenance = Maintenance.objects.all()
	context = {'maintenance':maintenance}
	return render(request, 'mainapp/home.html', context)


def createmain(request):
	form = MainForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = MainForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
				
	context = {'form':form}
	return render(request, 'mainapp/main_form.html', context)


	

def updatemain(request, pk):

	curritem = Maintenance.objects.get(id=pk)
	form = MainForm(instance=curritem)

	if request.method == 'POST':
		form = MainForm(request.POST, instance=curritem)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'mainapp/main_form.html', context)

def deletemain(request, pk):
	curritem = Maintenance.objects.get(id=pk)
	if request.method == "POST":
		curritem.delete()
		return redirect('/')

	context = {'item':curritem}
	return render(request, 'mainapp/delete.html', context)

def showannualreport(request):
	annualreport = AnnualReport.objects.all()
	context = {'annualreport':annualreport}

	return render(request, 'mainapp/annualreport.html', context)


def createannualrep(request):
	form = annualrepForm()
	if request.method == 'POST':
		form = annualrepForm(request.POST, request.FILES)
		print(form)
		if form.is_valid():
			form.save()
			return redirect('/')		      
	
	context = {'form':form}
	return render(request, 'mainapp/annualrep_form.html', context)