"""
This module contains the code for housing my methods
that are used in my automated mobile testing.
"""

import configparser
from appium import webdriver as appium_webdriver
from appium.webdriver.common.appiumby import AppiumBy
from combined_automation_methods import CombinedAutomationMethods

# Read the config file
config = configparser.ConfigParser()
config.read('config.ini')

APPIUM_PORT = config.get('Appium', 'port')
APPIUM_HOST = config.get('Appium', 'host')


class MobileAutomationMethods(CombinedAutomationMethods):
    """
    These are my mobile automation methods, and this is its class
    """
    def __init__(self):
        super().__init__()
        self.driver = None
        self.wait = None
        self.service = None

    def stop_service(self):
        """
        This stops the service
        """
        if self.driver is not None:
            self.driver.quit()
        self.service.stop()

    def create_android_driver(self, custom_opts=None):
        """
        Makes my android driver
        """
        options = {}
        options["appium:automationName"] = "UiAutomator2"
        options["appium:platformName"] = "Android"
        options["appium:deviceName"] = "emulator-5554"
        options["appium:browserName"] = "Chrome"
        options["appium:noReset"] = True
        options["appium:newCommandTimeout"] = 0
        options["appium:connectHardwareKeyboard"] = True

        if custom_opts is not None:
            for key in custom_opts:
                options[key] = custom_opts[key]

        self.driver = appium_webdriver.Remote(
           command_executor='http://localhost:4723',
           desired_capabilities=options
        )

    def clear_text(self, element):
        """
        Clears the text of an element
        """
        element.clear()

    def send_keys(self, element, text):
        """
        Sends keys/text to an element
        """
        element.send_keys(text)

    def get_text(self, element):
        """
        Retrieves the text of an element
        """
        return element.text

    def find_element_by_uiautomator(self, uiautomator_string):
        """
        Finds an element in the mobile app using an UiAutomator string
        """
        element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                           uiautomator_string
                                           )
        return element

    def find_element_by_xpath(self, selector):
        """
        Finds an element in the mobile app using XPATH
        """
        element = self.driver.find_element(AppiumBy.XPATH, selector)
        return element

    def enter_text(self, uiautomator_string, text):
        """
        Enters text into a field in the mobile app
        """
        element = self.find_element_by_uiautomator(
            uiautomator_string
            )
        self.clear_text(element)
        self.send_keys(element, text)

    def copy_text(self, uiautomator_string):
        """
        Copies text from a field in the mobile app
        """
        element = self.find_element_by_uiautomator(
            uiautomator_string
            )
        return self.get_text(element)
