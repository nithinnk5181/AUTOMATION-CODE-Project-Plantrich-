from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Approve_vendor:
    '''PageObjectives'''
    VIEW_VENDOR_ITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[12]/app-sidebar-nav-items/app-sidebar-nav-link[2]/a/app-sidebar-nav-link-content"
    APPROVE_BUTTON_XPATH="//table/tbody/tr[last()]/td[last()]/div/div[1]"
    DECLINE_BUTTON_XPATH="//table/tbody/tr[last()]/td[last()]/div/div[2]"
    CONFIRMATION_YES_XPATH="/html/body/modal-container/div/div/app-approval-confirmation/div/div[3]/button[1]"
    CONFIRMATION_YES_DECLINE_XPATH="/html/body/modal-container/div/div/app-decline-confirmation/div/div[3]/button[1]"
    LAST_PAGE_XPATH="//ngb-pagination//li[last()-1]"
    LAST_VENDOR_CODE_XPATH="//table/tbody/tr[last()]/td[2]"
    PAGE_COUNT_XPATH="//ngb-pagination//li"
    DECLINED_STATUS="//table/tbody/tr[last()]/td[last()]/div/div"



    def __init__(self,driver):
        self.driver=driver

    def Click_view_vendor(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.VIEW_VENDOR_ITEM_XPATH).click()

    def Approve_last_vendor(self):
        self.driver.find_element_by_xpath(self.APPROVE_BUTTON_XPATH).click()

    def Declain_last_vendor(self):
        self.driver.find_element_by_xpath(self.DECLINE_BUTTON_XPATH).click()

    def Confirm_yes(self):
        self.driver.find_element_by_xpath(self.CONFIRMATION_YES_XPATH).click()

    def Confirm_yes_declain(self):
        self.driver.find_element_by_xpath(self.CONFIRMATION_YES_DECLINE_XPATH).click()

    def check_approved(self):
        code=self.driver.find_element_by_xpath(self.LAST_VENDOR_CODE_XPATH)
        return code.text

    def check_Declined(self):
        code=self.driver.find_elements_by_xpath(self.DECLINED_STATUS)
        length=len(code)
        return length


    def Goto_last_page(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = self.driver.find_elements_by_xpath(self.PAGE_COUNT_XPATH)
        num=len(Page_count)
        for i in range(num):
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.LAST_PAGE_XPATH)))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            actions.click().perform()