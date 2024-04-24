from django.test import TestCase
from django.urls import reverse
# create your test here

class HomeViewTestCase(TestCase):

    def test_home_url(self):
        self.response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'index.html')


class AboutViewTestCase(TestCase):
    
    def test_about_url(self):
        self.response = self.client.get(reverse('about'))
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateNotUsed(self.response, 'home.html')

class ContactViewTestCase(TestCase):

    def test_contact_url(self):
        self.response = self.client.get(reverse('contact'))
        self.assertEqual(self.response.status_code, 404)
        self.assertTemlateUsed(self.response, 'contact.html')


class LoginTestCaseView(TestCase):
    
    def test_login_url(self):
        login_url = 'login'
        url2 = 'index'
        # data = {'tonny': 123}
        self.response = self.client.post(path   ='login', data={'tonny': 123})
        self.assertTrue(login_url, url2)
