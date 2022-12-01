from selenium.common import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)
        add_btn.click()
        try:
            self.solve_quiz_and_get_code()
        except NoAlertPresentException:
            pass
        self.compare_titles()
        self.compare_prices()

    def compare_titles(self):
        alert_product_title = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_TITLE).text
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        assert alert_product_title == product_title, "Alert title differs from the product one"

    def compare_prices(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_COST).text.split(" ")[2]
        basket_price = basket_price[:basket_price.index("\n")]
        assert product_price == basket_price, "Basket price differs from the product one"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_element(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Element didn't disappear"
