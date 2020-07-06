import os
import logging
import platform

from getgauge.python import before_scenario, after_scenario, custom_screenshot_writer, Screenshots, after_step
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from step_impl.utils.date_utils import timestamp


class Driver(object):

    logging.basicConfig(level=logging.INFO)
    driver = None

    @before_scenario
    def init(self):
        if os.getenv("BROWSER") == "CHROME":
            options = ChromeOptions()
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            if os.getenv("HEADLESS") == "True":
                options.add_argument("--headless")
                options.add_argument("--window-size=1920,4320")
            else:
                options.add_argument("--window-size=1280,1024")
            if platform.system() == "Linux":
                driver_path = "env/chrome/chromedriver/linux64/" + os.getenv("VERSION") + "/chromedriver"
            elif platform.system() == "Windows":
                driver_path = "env\\chrome\\chromedriver\\win32\\" + os.getenv("VERSION") + "\\chromedriver"
            # options.binary_location =
            Driver.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        elif os.getenv("BROWSER") == "FIREFOX":
            options = FirefoxOptions()
            if os.getenv("HEADLESS") == "True":
                options.add_argument("--headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=4320")
            else:
                options.add_argument("--width=1280")
                options.add_argument("--height=1024")
            if platform.system() == "Linux":
                driver_path = "env/firefox/geckodriver/linux64/" + os.getenv("VERSION") + "/geckodriver"
            elif platform.system() == "Windows":
                driver_path = "env\\firefox\\geckodriver\\win32\\" + os.getenv("VERSION") + "\\geckodriver"
            Driver.driver = webdriver.Firefox(executable_path=driver_path, options=options)

    @after_scenario
    def close(self):
        Driver.driver.close()


@custom_screenshot_writer
def take_screenshot():
    file_name = os.path.join(os.getenv("gauge_screenshots_dir"), ("screenshot-{0}.png".format(timestamp())))
    Driver.driver.save_screenshot(file_name)
    return os.path.basename(file_name)

@after_step
def after_step_screenshot():
    Screenshots.capture_screenshot()
