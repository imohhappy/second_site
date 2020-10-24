from django.test import TestCase
from django.utils import timezone
from .models import Vacancy, Post
from django.urls import reverse


class Vacancymodeltest(TestCase):
    def test_vacancy(self):
        vacancy = Vacancy.objects.create(title = 'henry', description = 'desperate')
        now = timezone.now()
        return self.assertLessEqual(vacancy.date_pub, timezone.now())


class Postmodeltest(TestCase):
    def setUp(self):
        self.vacancy = Vacancy.objects.create(title='name', description='desperate')

    def test_post(self):
        post = Post.objects.create(name='name', description='desperate', order=2,
                                   vacancy=self.vacancy)
        return self.assertIn(post, self.vacancy.post_set.all())


class Vacancyviewtest(TestCase):
    def test_vacancy(self):
        vacancy = Vacancy.objects.create(title = 'henry', description = 'desperate')

    def detailviewtest(self):
        response = self.client.get(reverse('job:detail'))
        self.assertEqual(response.status_code, 200)
        return self.assertIn(response, response.context['keep'])


class Posviewtest(TestCase):
    def setUp(self):
        self.vacancy = Vacancy.objects.create(title='name', description='desperate')

    def test_detail(self):
        post = Post.objects.create(name='name', description='desperate', order=2,
                                   vacancy=self.vacancy)
        return self.assertIn(post, self.vacancy.post_set.all())

    def detailview(self):
        response = self.client.get(reverse('job:postkeep'))
        self.assertEqual(response.status_code, 200)
        return self.assertIn(response, response.context['pit'])
