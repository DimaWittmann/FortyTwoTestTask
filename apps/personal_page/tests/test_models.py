from django.test import TestCase
from apps.personal_page.models import Person


class PersonModelTest(TestCase):
    fixtures = ["initial_data.json"]

    def test_retrieving_data(self):
        """
        Test if db contains personal information
        """

        person = Person.objects.all()
        self.assertEqual(person.count(), 1)
        self.assertEqual(person[0].name, "Dmytrii")
