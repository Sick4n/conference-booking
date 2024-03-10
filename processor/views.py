from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

@login_required(login_url='/designium-solutions/public/login')
def Index(request):
    
    return render(request, 'index.html')