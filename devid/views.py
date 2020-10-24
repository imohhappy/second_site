from django.shortcuts import render
from .forms import Marriageform
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def marriageview(request):
    personal = Marriageform()
    if request.method == 'POST':
        personal = Marriageform(request.POST)
        if personal.is_valid():
            personal.save()
            return HttpResponseRedirect(reverse('job:comment'))
    return render(request, 'pop.html', {'pen': personal})


def log(request):
    return render(request, 'log.html')
# Create your views here.
