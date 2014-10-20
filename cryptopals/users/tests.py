from django.test import TestCase
from django.test.client import Client
from models import User
import re

# Test aims
# Register user with email
# Register user with Facebook
# Check user public listing
# Change user listing details
# Check changed user listing removes user publicly

class HomeView(TestCase):
	def test_index(self):
		"""
		Check public home page works
		"""
		resp = self.client.get('/', follow=True)	
		self.assertEqual(resp.status_code, 200)
		self.assertIn('<div id="pal', resp.content)

class RegisterUser(TestCase):
	def test_register(self):
		"""
		Register new user and check user is listed on home page
		"""
		user = self.client.post('/accounts/signup', 
			{'username': 'testee',
			'email': 'theabstractarts+test@gmail.com',
			'password': 'testee'}, follow=True)
		self.assertEqual(mail.outbox[0].subject,
			'Confirm E-mail Address')
		email_body = mail.outbox[0].body
		activation_url = re.search(r'http[\S]*', email_body)
		"""
		Check user appears on home page
		"""
		resp = self.client.get('/', follow=True)
		self.assertEqual(resp.status_code, 200)
		self.assertIn('<div class="name-key">\
			<p class="username"><strong>testee', resp.body)

