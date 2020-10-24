from django.db import models
from django.urls import reverse


class Vacancy(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Title: {}'.format(self.title)
        #return 'Title:{}, description:{}, date_pub:{}'.format(self.title, self.description, self.date_pub)

    def get_absolute_url(self):
        return reverse("job:detail", kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'vacancies'


class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField(default=0)
    vacancy = models.ForeignKey(to=Vacancy, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}'. format(self.name, self.description, self.order)

    def get_absolute_url(self):
        return reverse("job:postkeep", kwargs={"vacancy_id": self.id, 'pk': self.pk})

    class Meta:
        ordering = ['order']


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone_num = models.PositiveIntegerField()
    E_mail = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name


# Create your models here.
