from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".btn-group>a.btn.btn-default")
    BASKET_MSG = (By.CSS_SELECTOR, "div#content_inner>p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "#id_registration-password2")
    # REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_PRODUCT = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    BASKET_COST = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
    ALERT_PRODUCT_TITLE = (By.CSS_SELECTOR, "div.alertinner>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
