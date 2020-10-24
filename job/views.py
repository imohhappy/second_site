from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Vacancy, Post
from django.views.generic import ListView
from django.views.generic import TemplateView, CreateView,  DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import Contactform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class Studentcreatview(CreateView):
    fields = ['title', 'description']
    model = Vacancy
    template_name = 'student.html'
    success_url = reverse_lazy('job:vacancy')


@login_required(login_url='/')
def contactview(request):
    contact = Contactform()
    if request.method == 'POST':
        contact = Contactform(request.POST)
        if contact.is_valid():
            contact.save()
            return HttpResponseRedirect(reverse('sign'))
    return render(request, 'comment.html', {'contact': contact})


def up(request):
    return render(request, 'update.html')

class Vacancyview(LoginRequiredMixin, ListView):
    model = Vacancy
    template_name = 'vacancy.html'

    def get_context_data(self, **kwargs):
        context = super(Vacancyview, self).get_context_data(**kwargs)
        context['var1'] = Vacancy.objects.all()
        return context


'''def vacancy(request):
    variable = Vacancy.objects.all()[:2]
    varable = Vacancy.objects.all()[3:5]
    return render(request, 'vacancy.html', {'dent':variable,'dent2':variable})
'''


class Vacancydetail(LoginRequiredMixin, DetailView):
    model = Vacancy
    context_object_name = 'keep'
    template_name = 'detail.html'


class VancancyUpdate(UpdateView):
    fields = ['title', 'description']
    model = Vacancy
    template_name = 'Vupdate.html'

class VancancyDelete(DeleteView):
    model = Vacancy
    success_url = reverse_lazy('job:vacancy')
    template_name = 'Vdelete.html'

class Postdetail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = "pit"
    template_name = 'postdetail.html'


class Contact(LoginRequiredMixin, TemplateView):
    template_name = 'contact.html'


@login_required(login_url='/')
def about(request):
    return render(request, 'about.html')


@login_required(login_url='/')
def close(request):
    return render(request, 'exit.html')



# Create your views here.
