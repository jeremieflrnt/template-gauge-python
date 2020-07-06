import logging
import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, \
    ElementNotSelectableException, StaleElementReferenceException, TimeoutException, \
    WebDriverException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from getgauge.python import Screenshots
from step_impl.utils.driver import Driver


def click_find_by_xpath(xpath, driver=None):
    if driver is None:
        driver = Driver.driver
    element = wait_for_element_to_be_clickable_find_by_xpath(xpath, driver)
    click(element, driver)


def click(element, driver=None):
    if driver is None:
        driver = Driver.driver
    try:
        WebDriverWait(driver, 5, 0.2).until(end_of_scroll(element))
        driver.execute_script("return arguments[0].scrollIntoView({block: \"center\"});", element)
        element.click()
    except ElementClickInterceptedException:
        wait_for_element_to_be_visible(element, driver)
        element.click()
    except ElementNotVisibleException:
        assert False, "ElementNotVisibleException"
    except ElementNotInteractableException:
        assert False, "ElementNotInteractableException"
    except ElementNotSelectableException:
        assert False, "ElementNotSelectableException"
    except StaleElementReferenceException:
        assert False, "StaleElementReferenceException"


def clear_and_send_keys_find_by_xpath(xpath, value, driver=None):
    if driver is None:
        driver = Driver.driver
    element = wait_for_elements_to_be_present_find_by_xpath(xpath, driver)[0]
    clear(element, driver)
    send_keys(element, value, driver)


def clear_and_send_keys(element, value, driver=None):
    if driver is None:
        driver = Driver.driver
    clear(element, driver)
    send_keys(element, value, driver)


def send_keys_find_by_xpath(xpath, value, driver=None):
    if driver is None:
        driver = Driver.driver
    element = wait_for_elements_to_be_present_find_by_xpath(xpath, driver)[0]
    send_keys(element, value, driver)


def send_keys(element, value, driver=None):
    if driver is None:
        driver = Driver.driver
    try:
        WebDriverWait(driver, 1, 0.1).until(end_of_scroll(element))
        driver.execute_script("return arguments[0].scrollIntoView({block: \"center\"});", element)
        element.send_keys(value)
    except ElementClickInterceptedException:
        assert False, "ElementClickInterceptedException"
    except ElementNotVisibleException:
        assert False, "ElementNotVisibleException"
    except ElementNotSelectableException:
        assert False, "ElementNotSelectableException"
    except StaleElementReferenceException:
        assert False, "StaleElementReferenceException"


def send_keys_slowly(element, value, delay, driver=None):
    if driver is None:
        driver = Driver.driver
    clear(element, driver)
    try:
        driver.execute_script("return arguments[0].scrollIntoView({block: \"center\"});", element)
        for character in value:
            element.send_keys(character)
            wait(delay)
    except ElementClickInterceptedException:
        assert False, "ElementClickInterceptedException"
    except ElementNotVisibleException:
        assert False, "ElementNotVisibleException"
    except ElementNotSelectableException:
        assert False, "ElementNotSelectableException"
    except StaleElementReferenceException:
        assert False, "StaleElementReferenceException"


def clear(element, driver=None):
    if driver is None:
        driver = Driver.driver
    if element.get_attribute("value") != "":
        click(element, driver)
        if isinstance(driver, webdriver.Chrome):
            ActionChains(driver).send_keys(Keys.HOME). \
                key_down(Keys.LEFT_SHIFT).send_keys(Keys.END).key_up(Keys.LEFT_SHIFT). \
                send_keys(Keys.DELETE). \
                send_keys(Keys.DELETE).perform()
        else:
            ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_Keys(
                Keys.DELETE).perform()


def wait_for_elements_to_be_present_find_by_xpath(xpath, driver=None):
    if driver is None:
        driver = Driver.driver
    try:
        return WebDriverWait(driver, 30, 0.1).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))
    except TimeoutException:
        logging.exception("TimeoutException")
        Screenshots.capture_screenshot()
        assert False, "L'élément n'est pas présent.\n" + "Vérifier la dernière capture.\n\n" + \
                      "Xpath élément concerné : \n" + xpath


def wait_for_element_to_be_visible(element, driver=None):
    if driver is None:
        driver = Driver.driver
    try:
        return WebDriverWait(driver, 30, 0.1).until(expected_conditions.visibility_of(element))
    except TimeoutException:
        logging.exception("TimeoutException")
        Screenshots.capture_screenshot()
        assert False, "L'élément n'est pas visible.\n" + "Vérifier la dernière capture.\n\n" + \
                      "Elément concerné : \n" + element


def wait_for_elements_to_be_visible_find_by_xpath(xpath, driver=None):
    if driver is None:
        driver = Driver.driver
    try:
        return WebDriverWait(driver, 30, 0.1).until(
            expected_conditions.visibility_of_any_elements_located((By.XPATH, xpath)))
    except TimeoutException:
        logging.exception("TimeoutException")
        Screenshots.capture_screenshot()
        assert False, "Aucun élément n'est visible.\n" + "Vérifier la dernière capture.\n\n" + \
                      "Xpath élément concerné : \n" + xpath


def wait_for_elements_to_be_visible_find_by_text(text, driver=None):
    if driver is None:
        driver = Driver.driver
    try:
        return WebDriverWait(driver, 30, 0.1).until(visibility_of_any_elements_located_by_text(text))
    except TimeoutException:
        logging.exception("TimeoutException")
        Screenshots.capture_screenshot()
        assert False, "Aucun élément n'est visible avec le texte recherché.\n" + "Vérifier la dernière capture.\n\n" + \
                      "texte concerné : \n" + text


def wait_for_element_to_be_clickable(element, driver=None):
    if driver is None:
        driver = Driver.driver
    try:
        return WebDriverWait(driver, 30, 0.1).until(
            expected_conditions.element_to_be_clickable((By.ID, element.get_attribute("id"))))
    except TimeoutException:
        logging.exception("TimeoutException")
        Screenshots.capture_screenshot()
        assert False, "L'élément n'est pas cliquable.\n" + "Vérifier la dernière capture.\n\n" + \
                      "Elément concerné : \n\n" + element.get_attribute("id")


def wait_for_element_to_be_clickable_find_by_xpath(xpath, driver=None):
    if driver is None:
        driver = Driver.driver
    try:
        return WebDriverWait(driver, 30, 0.1).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
    except TimeoutException:
        logging.exception("TimeoutException")
        Screenshots.capture_screenshot()
        assert False, "L'élément n'est pas cliquable.\n" + "Vérifier la dernière capture.\n\n" + \
                      "Locator élément concerné : \n\n" + xpath


def is_element_exist_find_by_xpath(xpath, driver=None):
    if driver is None:
        driver = Driver.driver
    return len(driver.find_elements_by_xpath(xpath)) > 0


def is_checked_jquery(element, driver=None):
    if driver is None:
        driver = Driver.driver
    return driver.execute_script("return arguments[0].checked;", element)


def clean_string_for_xpath(string):
    return "concat('" + string.replace("'", "', \"'\", '") + "', '')"


def wait(sec):
    time.sleep(sec)


class visibility_of_any_elements_located_by_text(object):
    """ An expectation for checking that there is at least one element visible
    on a web page.
    text is used to find the element
    returns the list of WebElements once they are located
    """

    def __init__(self, text):
        self.locator = (By.XPATH, "//*[text()[contains(.," + clean_string_for_xpath(text) + ")]]")

    def __call__(self, driver):
        return [element for element in _find_elements(driver, self.locator) if _element_if_visible(element)]


class end_of_scroll(object):
    """ An expectation for checking that the scroll is complete on a web page.
    element is the element used to check its coordinates
    returns True if the element is not moving, False otherwise.
    """

    def __init__(self, element):
        self.element = element
        self.coordinate_y = element.location.get("y")

    def __call__(self, driver):
        current_y = self.element.location.get("y")
        if self.coordinate_y == current_y:
            return True
        else:
            self.coordinate_y = current_y
            return False


def _element_if_visible(element, visibility=True):
    return element if element.is_displayed() == visibility else False


def _find_elements(driver, by):
    try:
        return driver.find_elements(*by)
    except WebDriverException as e:
        raise e
