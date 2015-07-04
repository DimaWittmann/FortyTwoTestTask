from django.test import TestCase
from django.core.urlresolvers import reverse


class PersonalPageTest(TestCase):
    fixtures = ['initial_data.json']

    def test_personal_page_renders_personal_page_template(self):
        """
        Test if view return correct template
        """
        response = self.client.get(reverse('personal_page'))
        self.assertTemplateUsed(response, 'personal_page/personal_page.html')


class RequestLogsPageTest(TestCase):
    fixtures = ['personal_page.json']

    def test_page_renders_correct_template(self):
        """
        Test if view return correct template
        """
        response = self.client.get(reverse('requests'))
        self.assertTemplateUsed(response, 'personal_page/logs.html')
