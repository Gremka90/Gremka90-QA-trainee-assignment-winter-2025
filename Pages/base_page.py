from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        return self.driver.get(self.URL)

    def get_current_url(self):
        return self.driver.current_url

    def refresh(self):
        return self.driver.refresh()

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    def wait_redrawing(self, locator, time=10):
        old_element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.driver, time).until(EC.staleness_of(old_element))
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))