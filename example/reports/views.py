from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('reports/index.html',
                              context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_staff)
def staff(request):
    return render_to_response('reports/staff.html',
                              context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
def superuser(request):
    return render_to_response('reports/superuser.html',
                              context_instance=RequestContext(request))
