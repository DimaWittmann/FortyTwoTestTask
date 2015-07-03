from selenium import webdriver

from django.test import LiveServerTestCase


class PersonalPageTest(LiveServerTestCase):
    fixtures = ['personal_page.json']

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(PersonalPageTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(PersonalPageTest, self).tearDown()

    def test_personal_page_content(self):
        """
        Test that user can see Personal page if user goes to /personal_page
        """
        # Open page with profile
        self.selenium.get('%s%s' % (self.live_server_url, '/personal_page'))
        self.assertIn('Personal page', self.selenium.title)
