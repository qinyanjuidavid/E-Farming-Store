from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from accounts.forms import RegistrationForm
from django.contrib import messages



def Registration(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST or None,request.FILES or None)
        if form.is_valid:
            form.save()
            messages.success(request,'Your account has successfully was successfully created')
            return HttpResponseRedirect('/accounts/login/')
    else:
        form=RegistrationForm()
    context={
    'form':form
    }
    return render(request,'accounts/register.html',context)
