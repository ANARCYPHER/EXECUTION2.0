#from django.shortcuts import render, redirect
#from .forms import SerialForm
#from django.http import HttpResponseRedirect

#def index(request):
 #   return render(request, 'index.html', {})

#def about(request):
#    return render(request, 'about.html', {})

#def doxing(request):
#    return render(request, 'doxing.html', {})

#def add_serial(request):
#    submitted = False
#    if request.method == "POST":
#        form = SerialForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return 	HttpResponseRedirect('/add_serial?submitted=True')
#        else:            
#            form = SerialForm
#3            if 'submitted' in request.GET:
#                submitted = True
#        return render(request, 'add_serial.html', {'form':form, 'submitted':submitted})

from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

