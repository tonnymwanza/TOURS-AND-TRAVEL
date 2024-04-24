from django.test import TestCase

from . models import Booking
from . models import Contact
from . models import Trending
# Create your tests here.

class ContactTestCase(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(name='tony', email='toni@gmail.com', subject='urgent', message='its urgent')

    def test_contact(self):
        self.assertEqual(self.contact.name, 'tony')
        self.assertEqual(self.contact.email, 'toni@gmail.com')
        self.assertEqual(self.contact.subject, 'urgent')
        self.assertEqual(self.contact.message, 'its urgent')


class BookingTestCase(TestCase):
    
    def setUp(self):
        self.booking = Booking.objects.create(
            destination='malawi',check_in='2024-07-09',check_out='2024-07-28',adults=3, children=5
        )

    def test_booking(self):
        self.assertTrue(self.booking.children)
        self.assertEqual(self.booking.destination, 'malawi')
        self.assertEqual(self.booking.check_in, '2024-07-09')
        self.assertEqual(self.booking.check_out, '2024-07-28')
        self.assertEqual(self.booking.adults, 3)

class TrendingTestCase(TestCase):
    
    def setUp(self):
        self.trending = Trending.objects.create(name='hotel', price=123, location='nyali', image='key.jpeg')

    def test_trending(self):
        self.assertTrue(self.trending.image)
        self.assertEqual(self.trending.name, 'hotel')
        self.assertEqual(self.trending.price, 123)
        self.assertEqual(self.trending.location, 'nyali')