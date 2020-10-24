from django.shortcuts import render
from django.views.generic import FormView, CreateView, RedirectView
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.urls import reverse_lazy
from . form import Signupform
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class Passwordchangeview(FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/Passwordchangeform.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class Passwordresetview(FormView):
    form_class = PasswordResetForm
    template_name = 'account/forgotenpassword.html'
    success_url = reverse_lazy('account:set')

class Setpasswordview(FormView):
    form_class = SetPasswordForm
    template_name = 'account/newpassword.html'
    success_url = reverse_lazy('account:login')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
            return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        return super().form_valid(form)


class Passwordview(FormView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('account:password')
    template_name = 'account/reset.html'


class Logoutview(RedirectView):
    url = reverse_lazy('devid:log')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(self, request, *args, **kwargs)


class Signupview(CreateView):
    form_class = Signupform
    template_name = 'account/signup.html'
    success_url = reverse_lazy('devid:case')


class Loginview(FormView):
    form_class = AuthenticationForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


# Create your views here.
