"""
This module tests the quasar.dev site using my mobile device
and the methods and elements are imported from their
respctive modules.
"""
import time
from automation_elements import AutomationElements
from mobile_automation_methods import MobileAutomationMethods

automation_methods = MobileAutomationMethods()
automation_methods.create_android_driver()
automation_elements = AutomationElements()


automation_methods.driver.get("http://quasar.dev")
time.sleep(8)

# Locate and click the "More" button
more_button = automation_methods.find_element_by_xpath(
    automation_elements.mobile_more_button_xpath
    )
more_button.click()

# Locate and click the "Docs" button
docs_button = automation_methods.find_element_by_xpath(
    automation_elements.mobile_docs_button_xpath
    )
docs_button.click()

hamburger_button = automation_methods.find_element_by_xpath(
    automation_elements.mobile_hamburger_xpath
    )
hamburger_button.click()

vue_components_button = automation_methods.find_element_by_xpath(
    automation_elements.mobile_vue_components_xpath
)
vue_components_button.click()

automation_methods.driver.quit()
