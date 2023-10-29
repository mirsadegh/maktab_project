from django.shortcuts import render
from website.forms import *
from django.contrib import messages

   
   
   
def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
        
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket did not submitted')    
    form = ContactForm()        
    return render(request, 'website/contact.html',{'form': form })

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    


