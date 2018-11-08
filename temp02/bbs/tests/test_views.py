from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..forms import NewThreadForm
from ..models import Bbs, Post, Thread
from ..views import bbs_threads, home, new_thread
from accounts.views import signup

class HomeTests(TestCase):
    def setUp(self):
        self.bbs = Bbs.objects.create(name='Django', description='Django BBS.')
        url = reverse('bbs:index')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    # def test_home_url_resolves_home_view(self):
    #     view = resolve('/')
    #     self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_threads_page(self):
        bbs_threads_url = reverse('bbs:bbs_threads', kwargs={'pk': self.bbs.pk})
        self.assertContains(self.response, 'href="{0}"'.format(bbs_threads_url))

class BbsThreadsTests(TestCase):
    def setUp(self):
        Bbs.objects.create(name='Django', description='Django BBS.')

    def test_bbs_threads_view_success_status_code(self):
        url = reverse('bbs:bbs_threads', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_bbs_threads_view_not_found_status_code(self):
        url = reverse('bbs:bbs_threads', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_bbs_threads_url_resolves_bbs_threads_view(self):
        view = resolve('/bbs/1/')
        self.assertEquals(view.func, bbs_threads)

    def test_bbs_threads_view_contains_navigation_links(self):
        bbs_threads_url = reverse('bbs:bbs_threads', kwargs={'pk': 1})
        response = self.client.get(bbs_threads_url)
        homepage_url = reverse('bbs:index')
        new_thread_url = reverse('bbs:new_thread', kwargs={'pk': 1})

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_thread_url))

class NewTopicTests(TestCase):
    def setUp(self):
        Bbs.objects.create(name='Django', description='Django BBS.')
        User.objects.create_user(username='john', email='john@example.com', password='123')

    def test_new_thread_view_success_status_code(self):
        url = reverse('bbs:new_thread', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_thread_view_not_found_status_code(self):
        url = reverse('bbs:new_thread', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_thread_url_resolves_bbs_threads_view(self):
        view = resolve('/bbs/1/new/')
        self.assertEquals(view.func, new_thread)

    def test_new_threads_view_contains_link_back_to_bbs_threads_view(self):
        new_thread_url = reverse('bbs:new_thread', kwargs={'pk': 1})
        bbs_threads_url = reverse('bbs:bbs_threads', kwargs={'pk': 1})
        response = self.client.get(new_thread_url)
        self.assertContains(response, 'href="{0}"'.format(bbs_threads_url))

    def test_csrf(self):
        url = reverse('bbs:new_thread', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_thread_valid_post_data(self):
        url = reverse('bbs:new_thread', kwargs={'pk': 1})
        data = {
            'name': 'Test name',
            'message': 'Lorem ipsum dolor sit amet'
        }
        response = self.client.post(url, data)
        self.assertTrue(Thread.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_thread_invalid_post_data(self):
        url = reverse('bbs:new_thread', kwargs={'pk': 1})
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 200)

    def test_new_thread_invalid_post_data_empty_fields(self):
        url = reverse('bbs:new_thread', kwargs={'pk': 1})
        # data = {
        #     'name': '',
        #     'message': ''
        # }
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        # self.assertFalse(Thread.objects.exists())
        # self.assertFalse(Post.objects.exists())
        self.assertTrue(form.errors)

    def test_contains_form(self):
        url = reverse('bbs:new_thread', kwargs={'pk': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewThreadForm)

class SignUpTest(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)
