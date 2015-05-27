from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_sign_up(self):
		# Edith has heard about a cool art cataloguing website.
		# She goes to check out the homepage
		self.browser.get('http://localhost:8081/')

		# She notices the page title and header mention the
		# name of the site
		self.assertIn('SuperList', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('SuperList', header_text)

		# She is invited to sign up straight away on the home page
		email_box = self.browser.find_element_by_name('signup_email')
		self.assertEqual(
				email_box.get_attribute('placeholder'),
				'e-mail address'
		)

		username_box = self.browser.find_element_by_name('signup_username')
		self.assertEqual(
				username_box.get_attribute('placeholder'),
				'username'
		)

		password_box = self.browser.find_element_by_name('signup_password')
		self.assertEqual(
				password_box.get_attribute('placeholder'),
				'password'
		)

		confirm_password_box = self.browser.find_element_by_name('signup_confirm_password')
		self.assertEqual(
				confirm_password_box.get_attribute('placeholder'),
				'confirm password'
		)

		# She signs up using the username edith@example.com, username edith, password guest123
		email_box.send_keys('edith@example.com')
		username_box.send_keys('edith')
		password_box.send_keys('guest')
		confirm_password_box.send_keys('guest')

		# Then she presses enter in the final box
		confirm_password_box.send_keys(Keys.ENTER)

		self.fail("Finish the test!")

if __name__ == '__main__':
	unittest.main()
