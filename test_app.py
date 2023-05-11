from selenium import webdriver
from selenium.webdriver.common.by import By
from classes.Trigger import Trigger
import pytest

link_url = "https://www.pcfactory.cl/producto/45780-gear-notebook-orchid-14-1-fhd-intel-i5-1135g7-8gb-256gb-ssd-windows-10"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(link_url)
    return driver


# Debe comprobar la url de la plataforma de pagos
def test_direc_to_to_pay( driver ):

    trigger = Trigger( driver )

    trigger.add_product_to_cart()
    trigger.fill_direction_input()
    trigger.fill_inputs_and_pay()
    assert 'mercadopago.cl' in driver.current_url 

# En icono de carro debe aparecer el producto agregado.
def test_product_in_car( driver ):

    trigger = Trigger( driver )
    trigger.add_product_to_cart()
    assert trigger.driver.find_element(by=By.CSS_SELECTOR, value=".added-products-indicator:nth-child(3)").text in "1" 



