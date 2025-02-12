from selenium.webdriver.common.by import By


class AnnouncementPageLocators:
    URL = 'http://tech-avito-intern.jumpingcrab.com/'
    CREATE_BUTTON = (By.XPATH, "//div[@class='chakra-stack css-1633cbu']/button[3]") #Локатор кнопки создать
    INPUT_NAME = (By.XPATH, "//input[@name='name']") #Локатор ввода названия товара
    INPUT_PRICE = (By.XPATH, "//section//input[@name='price']") #Локатор ввода цены
    INPUT_DESCRIPTION = (By.XPATH, "//section//input[@name='description']") #Локатор ввода описания
    INPUT_IMAGE_URL = (By.XPATH, "//section//input[@name='imageUrl']") #Локатор вводы ссылки на изображение
    BUTTON_SAVE = (By.XPATH, "//section//button[@type='submit']") #Локатор кнопки сохранения
    INPUT_SEARCH = (By.XPATH, "//input[@placeholder='Поиск по объявлениям']") #Локатор поискового ввода
    PRODUCT_CARD = (By.XPATH, "//div[@class='css-1cickmn']//div[@class='css-1n43xc7']") #Локатор найденного объявления
    EDIT_BUTTON = (By.XPATH, "//*[name()='svg' and @stroke='currentColor']") #Локатор кнопки редактирования
    NAME_PRODUCT_CARD = (By.CSS_SELECTOR, "H2") #Локатор имени в карточке