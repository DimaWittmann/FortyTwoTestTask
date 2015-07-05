from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.personal_page.forms import PersonForm


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


class EditPageTest(TestCase):

    def test_page_renders_correct_template(self):
        """
        Test if view return correct template
        """
        response = self.client.get(reverse('edit_page'))
        self.assertTemplateUsed(response, 'personal_page/edit_page.html')

    def test_view_uses_correct_form(self):
        """
        Test if view return correct form
        """
        response = self.client.get(reverse('edit_page'))
        self.assertIsInstance(response.context['form'], PersonForm)
