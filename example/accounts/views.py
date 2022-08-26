from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'

    def get_success_url(self):
        return reverse_lazy('accounts:profile')


class SignOutView(LogoutView):
    next_page = 'accounts:index'


class IndexView(TemplateView):
    template_name = 'accounts/index.html'


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


class SuperOnlyView(TemplateView):
    template_name = 'accounts/super_only.html'
