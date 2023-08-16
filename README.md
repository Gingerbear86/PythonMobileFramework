# PythonMobileFramework

This module contains automated testing scripts for the quasar.dev website using a mobile device. The scripts utilize methods and elements defined in respective modules.

Prerequisites

Python 3.x
Appium
Selenium
Pandas
Chrome browser (for mobile automation)

Installation

Clone or download this repository.
Install the required Python packages using pip
pip install appium-python-client selenium pandas
Configure the config.ini file with appropriate Appium settings, including port and host.

Usage

Run the script by executing the main module
python main.py
The script navigates to quasar.dev, clicks on various elements, and performs mobile automation tasks.

Structure

automation_elements.py: Contains locator information for automation elements.
mobile_automation_methods.py: Defines methods for mobile automation.
combined_automation_methods.py: Defines shared automation methods.
main.py: Main script to execute the mobile testing.

Acknowledgments

The code in this repository were created with a little help from Chat GPT by Jonathan Howard, an aspiring software developer with expertise in Agile Software Development and proficiency in various programming languages.
