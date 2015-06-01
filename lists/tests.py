from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from lists.views import home_page

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['signup_email'] = 'edith@example.com'
		request.POST['signup_username'] = 'edith'
		request.POST['signup_password'] = 'guest'
		request.POST['signup_confirm_password'] = 'guest'
		response = home_page(request)
		self.assertIn('edith', response.content.decode())
		expected_html = render_to_string('home.html', {
			'new_username': 'edith'
		})
		self.assertEqual(response.content.decode(), expected_html)

class UserModelTest(TestCase):

	def test_saving_new_user(self):
		new_user = User.objects.create_user('edith', 'edith@example.com', 'guest')
		new_user.save()
		my_users = User.objects.all()
		self.assertEqual(my_users.count(), 1)

		first_user = my_users[0]
		self.assertEqual(first_user.first_name, 'edith')
		self.assertEqual(first_user.email, 'edith@example.com')
