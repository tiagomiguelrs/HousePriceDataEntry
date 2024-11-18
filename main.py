import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data_constructor import DataConstructor
from form_filler import FormFiller

STATIC_ZILLOW_ADDRESS = "https://appbrewery.github.io/Zillow-Clone/"
HEADER = {
    "Accept-Language": "pt-PT",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}


# Function's domain ----------------------------------------------------------------------------------------------------
def reshape_prices(price_text):
    """Reshapes the text from the BeautifulSoup scrape to match the format $xxxxx"""
    return price_text.strip().replace("/mo", "").split("+")[0].replace(",", "")

# ----------------------------------------------------------------------------------------------------------------------
response = requests.get(STATIC_ZILLOW_ADDRESS)
# print(response.content)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

# Find data in soup ----------------------------------------------------------------------------------------------------
soup_addresses = soup.find_all(name="address")
# print(addresses)
soup_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
# print(soup_prices)
soup_links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
# print(soup_links)

# Format data ----------------------------------------------------------------------------------------------------------
addresses = [address.getText().strip().replace(" |", ",") for address in soup_addresses]

prices = []
for price in soup_prices:
    prices.append(reshape_prices(price.getText()))

links = [link.get("href") for link in soup_links]

# print(len(addresses), len(prices), len(links))    # 44 44 44

# Construct data -------------------------------------------------------------------------------------------------------
house_data = []
for address, price, link in zip(addresses, prices, links):
    house_data.append(DataConstructor(address, price, link))

# print(data[0], data[0].price)

# Load driver ----------------------------------------------------------------------------------------------------------
chrome_driver_path = ChromeDriverManager().install()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach",
                                       value=True)  # Keep the browser open when the script finishes - unless you use driver.quit()

service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

# Fill form with all data ----------------------------------------------------------------------------------------------
for data in house_data:
    # Opens a new tab
    driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.CONTROL + 't')
    form = FormFiller(data, driver)
    form.fill_form()
    # Closes the opened tab
    driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.CONTROL + 'w')
