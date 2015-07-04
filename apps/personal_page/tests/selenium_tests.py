from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase

from apps.personal_page import models


class BaseTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(BaseTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(BaseTest, self).tearDown()


class PersonalPageTest(BaseTest):
    fixtures = ['personal_page.json']

    def test_personal_page_content(self):
        """
        Test that user can see Personal page if user goes to /personal_page
        """
        # Open page with profile
        self.selenium.get('%s%s' % (self.live_server_url,
                                    reverse('personal_page')))
        self.assertIn('Personal page', self.selenium.title)


class LogsPageTest(BaseTest):
    fixtures = ['personal_page.json']

    def load_page(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('requests')))
        try:
            WebDriverWait(self.selenium, 10).until(
                ec.presence_of_element_located((By.TAG_NAME, "td"))
            )
        except TimeoutException:
            pass

    def test_page_renders_10_logs_from_db(self):
        """
        Test if previously added logs renders on page
        """
        self.load_page()

        logs_count = models.RequestLog.objects.count()
        rendered_logs_count = len(self.selenium
                                  .find_elements_by_xpath('//tbody/tr'))

        self.assertTrue(rendered_logs_count == 10 or
                        rendered_logs_count == logs_count)

    def test_page_update_list_of_logs_asynchronously(self):
        """
        Test if new log loads on the page asynchronously
        """
        # User1 goes to page with logs
        self.load_page()
        # the first request is request made by user1
        first = self.selenium.find_element_by_xpath("//tbody/tr[1]/td[1]")
        self.assertEqual(first.text, reverse('requests'))

        # User2 goes to page with personal information
        new_selenium = webdriver.Firefox()
        new_selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        new_selenium.quit()

        # User1 sees new request /admin/
        try:
            WebDriverWait(self.selenium, 11).until(
                ec.presence_of_element_located((By.XPATH,
                                                "//td[text()='/admin/']"))
            )
        except TimeoutException:
            self.fail("/admin/ did not appear")
