from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Signupform
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse


def signupview(request):
    form = Signupform()
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            '''send_mail()
            subject = 'new email'
            message = ''
            EmailFrom = 'site.com'
            EmailTo = 'mysite.com'''

            send_mail('message by{}'.format(form.cleaned_data['name']), form.cleaned_data['password'], '{name}<{email}>'.format(**form.cleaned_data), ['sirwhiteonline@gmial.com'])
            return HttpResponseRedirect(reverse('job:comment'))
    return render(request, 'signup.html', {'morm': form})


class Home(TemplateView):
    template_name = 'home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testing'] = 'just testing'
        context['email'] = 'test@gmail.com'
        return context


def learning(request):
    return render(request, 'index.html')