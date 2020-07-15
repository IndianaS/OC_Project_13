from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False


class ChromeFunctionalTestCases(StaticLiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(self.live_server_url)

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        User = get_user_model()
        User.objects.create_user(
            username="UserTest", password="PasswordTest&")

    def test_user_can_connect_and_disconnect(self):
        self.driver.find_element_by_link_text("Connexion").click()
        self.driver.find_element_by_css_selector(
            "#id_username").send_keys("UserTest")
        self.driver.find_element_by_css_selector(
            "#id_password").send_keys("PasswordTest&")
        self.driver.find_element_by_css_selector("#button-submit").click()
        logout = self.driver.find_element_by_link_text("Deconnexion").click()
        logout_classes = logout.get_attribute("class")
        self.assertIn("fa-sign-out-alt", logout_classes,
                      "Disconnect icon should be available.")
