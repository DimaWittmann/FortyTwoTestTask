from django.test import TestCase
from apps.personal_page.models import Person

class PersonModelTest(TestCase):
    fixtures = ["personal_page.json"]

    def test_retrieving_data(self):

        person = Person.objects.all()
        self.assertEqual(person.count(), 1)
        self.assertEqual(person[0].name, "Dmytrii")
