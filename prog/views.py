from django.shortcuts import render,redirect
from . import models
from django.http import HttpResponse
from .forms import ProgressForm
from .models import ProgressModel
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

def index (request):
    return render (request,'index.html')

def show (request):

    context ={}
    # context
    Fields = ProgressModel.objects.all()
    # Fields =  ProgressForm(request.POST)
    # add the dictionary during initialization
    context = {'data' : Fields}
         

    return render (request, 'show.html',context)

def showdata(request,id):
    data = ProgressModel.objects.filter(id=id)
    context= {'showme':data[0]}
    print(context)
    return render(request,'showdata.html',context)
    
def add (request):
    context ={}
    
    form = ProgressForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect ('show')

    # context['form']= form
    args = {}
    args.update(csrf(request))
    args['form'] = form


    return render (request,'add2.html', args)

    
