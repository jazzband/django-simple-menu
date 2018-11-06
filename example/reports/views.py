from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.template import RequestContext

def index(request):
    return render(request, 'reports/index.html')

@user_passes_test(lambda u: u.is_staff)
def staff(request):
    return render(request, 'reports/staff.html')

@user_passes_test(lambda u: u.is_superuser)
def superuser(request):
    return render(request, 'reports/superuser.html')
