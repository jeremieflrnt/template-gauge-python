import os
import logging
from getgauge.python import step, Screenshots, Messages
from selenium.webdriver.common.keys import Keys

from step_impl.utils.driver import Driver
from step_impl.utils.selenium_utils import wait, send_keys_find_by_xpath, click_find_by_xpath


@step("Accéder à Google")
def acceder_a_google():
    Driver.driver.get(os.getenv("SUT_URL"))


@step("Faire une recherche pour : <rechercher>")
def faire_une_recherche(rechercher):
    send_keys_find_by_xpath("//input[@title='Rechercher']", rechercher)
    wait(0.1)
    Driver.driver.find_element_by_xpath("//input[@title='Rechercher']").send_keys(Keys.ENTER)


@step("Aller sur le 1er lien de la recherche")
def aller_premier_resultat():
    click_find_by_xpath("//h1[text()='Résultats de recherche']/parent::div//a[1]")


@step("Vérifier qu'on est sur le site du projet github")
def verifier_site_projet_github():
    titre = Driver.driver.title
    logging.info("le titre de la page est : " + titre)
    Messages.write_message("le titre de la page est : " + titre)
    Screenshots.capture_screenshot()
    assert titre == "GitHub - getgauge/gauge-python: Python language runner for Gauge", "Mauvaise page"
