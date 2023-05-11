import time
from selenium.webdriver.common.by import By 
from selenium.webdriver import Keys


class Trigger:

    def __init__(self, driver) -> None:
        self.driver = driver

    def add_product_to_cart( self ):
        add_to_cart_button = self.driver.find_element(by=By.ID, value="addtocart_45780_1")
        add_to_cart_button.click()

        buy_now_button = self.driver.find_element(by=By.ID, value="pagar_ahora")
        buy_now_button.click()

        invited_button = self.driver.find_element(by=By.ID, value="btn_invitado")
        invited_button.click()

        send_product_option = self.driver.find_element(by=By.ID, value="accordion2") 
        send_product_option.click()

    def fill_direction_input( self ):

        input_autocomplete_direction = self.driver.find_element(by=By.ID, value="autocomplete")
        input_autocomplete_direction.click()

        input_autocomplete_direction.send_keys("Salvador gutierrez 4815")
        time.sleep(3)
        input_autocomplete_direction.send_keys( Keys.DOWN )
        input_autocomplete_direction.send_keys( Keys.DOWN )
        input_autocomplete_direction.send_keys( Keys.ENTER )
        time.sleep(4)

        input_street_number = self.driver.find_element(by=By.ID, value="street_number")
        input_street_number.send_keys("4815")


        save_direction_button = self.driver.find_element(by=By.ID, value="guardar_direccion")
        save_direction_button.click()
        time.sleep(4)
        continue_to_pay_button = self.driver.find_element(by=By.ID, value="btn_continuar_pago")
        continue_to_pay_button.click()
        time.sleep(4)


    def fill_inputs_and_pay( self ):

        input_rut = self.driver.find_element(by=By.ID, value="id_rut_quien_compra")
        input_rut.send_keys("19281869-9")

        input_name = self.driver.find_element(by=By.XPATH, value="//input[@id='id_nombre_quien_compra']")
        input_name.send_keys("Matías")

        input_phone = self.driver.find_element(by=By.ID, value="id_fono_quien_compra")
        input_phone.send_keys("988984972")

        input_email = self.driver.find_element(by=By.ID, value="id_email_quien_compra")
        input_email.send_keys("mabarca@softwarereservo.com")
        input_email2 = self.driver.find_element(by=By.ID, value="cod_valid_email")
        input_email2.send_keys("mabarca@softwarereservo.com")

        input_pay = self.driver.find_element(by=By.CSS_SELECTOR, value="input[value=MERCADOPAGO]")
        input_pay.click()

        continue_to_pay_button = self.driver.find_element(by=By.ID, value="btn_continuar_pago")
        continue_to_pay_button.click()
        time.sleep(12)

