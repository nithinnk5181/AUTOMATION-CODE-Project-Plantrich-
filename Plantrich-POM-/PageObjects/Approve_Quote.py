from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Approve_quote:
    """PageObjectives"""
    VIEW_REQUISITION_MENU_ITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[4]/app-sidebar-nav-items/app-sidebar-nav-link[5]/a/app-sidebar-nav-link-content"
    APPROVE_ACTION_BUTTON_ON_TBLE_FIRST_RAW="//table[@class='table table-striped']/tbody/tr[1]/td[last()]/div"
    APPROVE_BUTTON_FOR_FIRST_RAW="//table[@class='table table-striped']/tbody/tr[last()]/td[last()]/div/div[1]/div/button[text()=' Approve']"
    DECLAIN_BUTTON_FOR_FIRST_RAW="//table[@class='table table-striped']/tbody/tr[last()]/td[last()]/div/div[2]/div/button[text()=' Decline']"

    def __init__(self,driver):
        self.driver=driver

    def click_view_quote(self):
        self.driver.find_element_by_xpath(self.VIEW_REQUISITION_MENU_ITEM_XPATH).click()

    def Goto_Approve_quote_page(self):
        element=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.APPROVE_ACTION_BUTTON_ON_TBLE_FIRST_RAW)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def Click_Approve_quote(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.APPROVE_BUTTON_FOR_FIRST_RAW)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def Click_Declain_quote(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.DECLAIN_BUTTON_FOR_FIRST_RAW)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()


