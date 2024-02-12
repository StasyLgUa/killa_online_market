from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self):
        button = self.driver.find_element(By.XPATH, "//div[@id='logo']")
        button.click()

    def open_about(self):
        button_about = self.driver.find_element(By.XPATH, "//header//ul[contains(@class,'top-menu')]/li/a[contains(@href,'o-nas.html')]")
        button_about.click()

    def open_delivery_and_payment(self):
        button_delivery = self.driver.find_element(By.XPATH, "//header//ul[contains(@class,'top-menu')]/li/a[contains(@href,'dostavka-i-oplata.html')]")
        button_delivery.click()

    def open_return_or_exchange(self):
        button_return = self.driver.find_element(By.XPATH, "//header//ul[contains(@class,'top-menu')]/li/a[contains(@href,'vozvrat-zamena.html')]")
        button_return.click()

    def open_contacts(self):
        button_contacts = self.driver.find_element(By.XPATH, "//header//ul[contains(@class,'top-menu')]/li/a[contains(@href,'kontakty.html')]")
        button_contacts.click()

    def open_help(self):
        button_help = self.driver.find_element(By.XPATH, "//header//ul[contains(@class,'top-menu')]/li/a[contains(@href,'help.html')]")
        button_help.click()

    def open_reviews(self):
        button_reviews = self.driver.find_element(By.XPATH, "//header//ul[contains(@class,'top-menu')]/li/a[contains(@href,'testimonial')]")
        button_reviews.click()

    def open_dropship(self):
        button_dropship = self.driver.find_element(By.XPATH, "//header//ul[contains(@class,'top-menu')]/li/a[contains(@href,'drop.html')]")
        button_dropship.click()


class OpenTouristEquipment(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_tourist_page(self):
        category_button = self.driver.find_element(By.XPATH, "//div[contains(@class,'col-sm-3')]/div[contains(@class, 'mainmenu')]")
        category_button.click()
        button_tourist_equipment = self.driver.find_element(By.XPATH, "//div[contains(@class, 'mainmenu ')]/ul[contains(@class,'list-unstyled')]/li/a[contains(@href,'/katalog/pohodnoe-snaryazhenie')]")
        button_tourist_equipment.click()

class TouristEquipment(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def check_tourist_equipment_category_list(self):
        tourist_equipment_list = []
        labels = self.driver.find_elements(By.XPATH, "//div[contains(@class,'row')]/ul/li/div/a[contains(@href,'/katalog/')]")
        for label in labels:
            tourist_equipment_list.append(label.text)
            number_of_list = len(tourist_equipment_list)
        return number_of_list

    def images_equipments(self):
        list_of_links = []
        not_displayed_img = self.driver.find_elements(By.XPATH, "//div[contains(@class,'row')]/ul/li/div/a[contains(@href,'/katalog/')]/img[contains(@src,'placeholder')]")
        links = self.driver.find_elements(By.XPATH,"//div[contains(@class,'row')]/ul/li/div/a[contains(@href,'/katalog/')]")
        for img in not_displayed_img:
           #list_of_links.append(img)
            for link in links:
                list_of_links.append(link.text)
            return list_of_links

    def open_generators_and_charging_stations_link(self):
        generators_and_charging_stations_link = self.driver.find_element(By.XPATH, "//div[contains(@class,'row')]/ul/li/div/a[contains(@href,'/katalog/pohodnoe-snaryazhenie/generatoryi-i-zaryadnyie-stantsii')]")
        generators_and_charging_stations_link.click()


    def check_images_for_items(self):
        list_of_items=[]
        items = self.driver.find_elements(By.XPATH, "//div[contains(@class,'product-grid')]/div/div/div/a[contains(@href,'https://killa.com.ua/uk/')]")
        for item in items:
            list_of_items.append(item)
            return list_of_items
        if len(list_of_items) == 0:
            print("All images are displayed")


    def click_on_list_of_generators(self):
        list_of_generators = self.driver.find_element(By.XPATH, "//div/a[contains(@href,'/katalog/pohodnoe-snaryazhenie/generatoryi-i-zaryadnyie-stantsii/generatoryi/')]")
        list_of_generators.click()

    def check_tourist_items_equipment_list(self):
        tourist_items_equipment_list = []
        items = self.driver.find_elements(By.XPATH, "//div[contains(@class,'product-grid')]/div/div/div/a[contains(@href,'https://killa.com.ua/uk/')]")
        for item in items:
            tourist_items_equipment_list.append(item.title)
            number_of_list = len(tourist_items_equipment_list)
        return number_of_list

