from django.test import TestCase


class PersonalPageTest(TestCase):
    fixtures = ['initial_data.json']

    def test_personal_page_renders_personal_page_template(self):
        """
        Test if view return correct template
        """
        response = self.client.get('/personal_page/')
        self.assertTemplateUsed(response, 'personal_page/personal_page.html')
