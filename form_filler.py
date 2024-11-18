from selenium import webdriver
from selenium.webdriver.common.by import By
from data_constructor import DataConstructor

FORM_LINK = "https://forms.gle/tGmmzzFdueqBKW8s8"
ADDRESS_INPUT_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
PRICE_INPUT_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
LINK_INPUT_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
SEND_BUTTON_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'


class FormFiller:
    """
    This class fills the Google form with the address, price and link of every apartment.
    It must be called for every piece of data.
    """

    def __init__(self, data: DataConstructor, driver: webdriver.Chrome):
        self.data = data
        self.driver = driver
        # implicit_wait makes the driver wait up to 5 seconds for the html element to appear before raising an error
        self.driver.implicitly_wait(5)

    def input_data(self, data_value: str, xpath_value: str):
        """Populates the input elements in the form web page."""
        data_input = self.driver.find_element(by=By.XPATH, value=xpath_value)
        data_input.send_keys(data_value)

    def fill_form(self):
        """Fills in the form using the methods above and clicks the "send" button to send the data to a Google sheet."""
        self.driver.get(FORM_LINK)
        self.input_data(self.data.address, ADDRESS_INPUT_XPATH)
        self.input_data(self.data.price, PRICE_INPUT_XPATH)
        self.input_data(self.data.link, LINK_INPUT_XPATH)
        self.driver.find_element(by=By.XPATH, value=SEND_BUTTON_XPATH).click()
