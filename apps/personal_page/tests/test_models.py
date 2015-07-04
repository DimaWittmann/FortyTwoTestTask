from django.test import TestCase

from apps.personal_page.models import Person, RequestLog


class PersonModelTest(TestCase):
    fixtures = ["initial_data.json"]

    def test_retrieving_data(self):
        """
        Test if db contains personal information
        """

        person = Person.objects.all()
        self.assertEqual(person.count(), 1)
        self.assertEqual(person[0].name, "Dmytrii")

    def test_saving_data(self):
        """
        Test that db updates data
        """
        new_name = "Vitja"

        person = Person.objects.first()
        person.name = "Vitja"
        person.save()

        person_with_new_name = Person.objects.first()
        self.assertEqual(person_with_new_name.name, new_name)


class RequestLogModelTest(TestCase):

    def test_adding_and_retrieving_data(self):
        """
        Test if db can save and return data
        """
        log = RequestLog()
        log.body = "{id: 25}"
        log.encoding = "utf-8"
        log.method = "GET"
        log.path = "/path"

        log.save()

        self.assertEqual(RequestLog.objects.count(), 1)
        self.assertEqual(RequestLog.objects.all()[0].path, "/path")
