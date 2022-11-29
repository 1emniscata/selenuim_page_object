from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def go_to_basket(self):
        basket_btn = self.browser.find_element(*BasePageLocators.BASKET)
        basket_link = basket_btn.get_attribute("href")
        self.open(basket_link)

    def get_basket_msg(self) -> str:
        basket_msg = self.browser.find_element(*BasePageLocators.BASKET_MSG).text
        return basket_msg