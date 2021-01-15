from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.shortcuts import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False


class ChromeFunctionalTestCases(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        User = get_user_model()
        User.objects.create_user(
            username="UserTest", password="PasswordTest&7722"
        )

    def tearDown(self):
        self.driver.quit()

    def test_user_can_connect_and_disconnect(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_id("login-link").click()
        self.driver.find_element_by_id("id_username").send_keys("UserTest")
        self.driver.find_element_by_id("id_password").send_keys(
            "PasswordTest&7722"
        )
        self.driver.find_element_by_id("button-submit").click()
        logout = self.driver.find_element_by_id("logout-link").click()

    def test_user_add_figurine(self):
        self.driver.get(self.live_server_url + reverse("figurines:add_figurine"))
        self.driver.find_element_by_id("id_username").send_keys("UserTest")
        self.driver.find_element_by_id("id_password").send_keys(
            "PasswordTest&7722"
        )
        self.driver.find_element_by_id("button-submit").click()
        self.driver.find_element_by_id("id_figurine_number").send_keys("1")
        self.driver.find_element_by_id("id_category").send_keys("Super heroes")
        self.driver.find_element_by_id("id_name").send_keys("Batman")
        self.driver.find_element_by_id("button-submit-addfigurine").click()

    def test_search_friend(self):
        self.driver.get(self.live_server_url + reverse("users:friends_list"))
        self.driver.find_element_by_id("id_username").send_keys("UserTest")
        self.driver.find_element_by_id("id_password").send_keys(
            "PasswordTest&7722"
        )
        self.driver.find_element_by_id("button-submit").click()
        self.driver.find_element_by_id("collection_user").send_keys(
            "UserAddTest"
        )
        self.driver.find_element_by_id("search-friend").click()
