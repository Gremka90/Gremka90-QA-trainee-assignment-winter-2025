import pytest
from Pages.announcement_page import AnnouncementPage


def test_create_announcement(driver):
    announcement_page = AnnouncementPage(driver)
    announcement_page.open()
    announcement_page.click_create_button()
    announcement_page.enter_name("Шорты")
    announcement_page.enter_price('1200')
    announcement_page.enter_description('б/у')
    announcement_page.enter_image_url("https://tvoe.ru/img/1uf8dvh/product/754/1005/8/4670080054185-0.jpg")
    announcement_page.click_save_button()
    announcement_page.refresh()
    announcement_page.enter_search("Шорты")
    announcement_page.wait_redrawing_product_card()
    assert announcement_page.search_first_price_on_product_card()[:-1] == '1200'


@pytest.mark.parametrize("create_test_data", [
    {
        'createdAt': "2025-02-10T20:55:36.891Z",
        'description': "б/у",
        'imageUrl': "https://tvoe.ru/img/1uf8dvh/product/754/1005/8/4670080054185-0.jpg",
        'likes': 2,
        'name': "Шорты",
        'price': "1200",
        'views': 3
    }
],  indirect=True)
def test_editing_announcement(driver, create_test_data):
    new_name = 'Шорты2'
    test_data_id = create_test_data
    announcement_page = AnnouncementPage(driver)
    announcement_page.open_advertisement_by_id(test_data_id)
    old_name = announcement_page.get_name_advertisement()
    announcement_page.click_edit_button()
    announcement_page.clear_input_name()
    announcement_page.enter_name(new_name)
    announcement_page.click_edit_button()
    assert old_name != new_name

@pytest.mark.parametrize("create_test_data", [
    {
        'createdAt': "2025-02-12T20:55:36.891Z",
        'description': "Новое",
        'imageUrl': "https://tvoe.ru/img/1uf8dvh/product/754/1005/8/4670080054185-0.jpg",
        'likes': 2,
        'name': "Шорты2",
        'price': "1300",
        'views': 3
    }
],  indirect=True)
def test_find_announcement(driver, create_test_data):
    test_data_id = create_test_data
    announcement_page = AnnouncementPage(driver)
    announcement_page.open()
    announcement_page.enter_search("Шорты2")
    announcement_page.wait_redrawing_product_card()
    announcement_page.click_product_card()
    current_url = announcement_page.get_current_url()
    assert current_url.replace("http://tech-avito-intern.jumpingcrab.com/advertisements/", '') == test_data_id
