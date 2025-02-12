from Pages.base_page import BasePage
from Locators.announcement_locator import AnnouncementPageLocators

class AnnouncementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AnnouncementPageLocators()

    def open(self):
        self.driver.get(self.locators.URL)

    def open_advertisement_by_id(self, advertisement_id):
        url = f'http://tech-avito-intern.jumpingcrab.com/advertisements/{advertisement_id}'
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def click_create_button(self):
        create_button = self.find_element(self.locators.CREATE_BUTTON)
        create_button.click()

    def click_save_button(self):
        create_button = self.find_element(self.locators.BUTTON_SAVE)
        create_button.click()

    def click_edit_button(self):
        create_button = self.find_element(self.locators.EDIT_BUTTON)
        create_button.click()

    def click_product_card(self):
        create_button = self.find_element(self.locators.PRODUCT_CARD)
        create_button.click()

    def enter_name(self, name):
        input_name = self.find_element(self.locators.INPUT_NAME)
        input_name.send_keys(name)

    def enter_description(self, description):
        input_description = self.find_element(self.locators.INPUT_DESCRIPTION)
        input_description.send_keys(description)

    def enter_price(self, price):
        input_price = self.find_element(self.locators.INPUT_PRICE)
        input_price.send_keys(price)

    def enter_image_url(self, image_url):
        input_image_url = self.find_element(self.locators.INPUT_IMAGE_URL)
        input_image_url.send_keys(image_url)

    def enter_search(self, name2):
        input_search = self.find_clickable_element(self.locators.INPUT_SEARCH)
        input_search.send_keys(name2)

    def clear_input_name(self):
        input_name = self.find_clickable_element(self.locators.INPUT_NAME)
        input_name.clear()

    def wait_redrawing_product_card(self):
        new_element = self.wait_redrawing(self.locators.PRODUCT_CARD)
        return new_element

    def search_first_price_on_product_card(self):
        search_price = self.find_element(self.locators.PRODUCT_CARD)
        return search_price.text

    def get_name_advertisement(self):
        return self.find_element(self.locators.NAME_PRODUCT_CARD)