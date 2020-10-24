from django import template
from job.models import Vacancy, Post


register = template.Library()


@register.simple_tag()
def new_vacancy():
    return Vacancy.objects.latest('date_pub')



