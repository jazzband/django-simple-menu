from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext

def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'registration/profile.html')
