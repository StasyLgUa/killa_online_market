from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from helper.pages.base import *

driver = webdriver.Chrome()

option = Options()
option.add_argument("--start-maximized")
prefs = {"profile.default_content_setting_values.notifications": 1}
option.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=option)

mensa_norway_url = "https://killa.com.ua/"
driver.get(mensa_norway_url)
driver.maximize_window()


home = BasePage(driver)
time.sleep(3)
# home.open_about()
# time.sleep(3)
# home.open_homepage()
# time.sleep(10)
# home.open_delivery_and_payment()
# time.sleep(3)
# home.open_return_or_exchange()
# time.sleep(3)
# home.open_contacts()
# time.sleep(3)
# home.open_help()
# time.sleep(3)
# home.open_reviews()
# time.sleep(3)
# home.open_dropship()
# time.sleep(3)
tourist = OpenTouristEquipment(driver)
tlist = TouristEquipment(driver)
tourist.open_tourist_page()
time.sleep(5)


print(tlist.check_tourist_equipment_category_list())
time.sleep(5)

print(tlist.images_equipments())
time.sleep(5)

tlist.open_generators_and_charging_stations_link()
time.sleep(3)

print(tlist.images_equipments())
time.sleep(3)

print(tlist.check_images_for_items())
time.sleep(3)

tlist.click_on_list_of_generators()
time.sleep(3)


print((tlist.check_images_for_items()))
time.sleep(3)

print((tlist.check_tourist_items_equipment_list()))
time.sleep(3)


