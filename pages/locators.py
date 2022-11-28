from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_PRODUCT = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    BASKET_COST = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
    ALERT_PRODUCT_TITLE = (By.CSS_SELECTOR, "div.alertinner>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
