from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))

@login_required
def profile(request):
    return render_to_response('registration/profile.html',
                              context_instance=RequestContext(request))
