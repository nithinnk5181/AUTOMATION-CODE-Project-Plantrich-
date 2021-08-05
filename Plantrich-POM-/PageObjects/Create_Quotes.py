from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class CreateQuotes:
    '''PageObjectives'''
    CREATE_QUOTES_DROPDOWNBUTTON_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[4]/app-sidebar-nav-items/app-sidebar-nav-link[4]/a"
    QUOTE_ACTION_XPATH="//table[@class='table table-striped']/tbody/tr[1]/td[last()]/div/div/div/*[name()='svg']"
    SEARCH_VENDOR_LABEL_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-requisition-quote/div/div[2]/div/div[2]/form/div[1]/div[2]"
    SERACH_VENDOR_TEXTBOX_XPATH='//*[@id="mat-dialog-0"]/app-search-vendor/div/div[2]/div/div[2]/form/mat-form-field/div/mat-form-field/input'
    VENDOR_DATA_SELECT="//mat-option/span"
    PRICE_PROD1_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-requisition-quote/div/div[2]/div/div[2]/form/div[6]/table/tbody/tr[1]/td[5]/input"
    PRICE_PROD2_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-requisition-quote/div/div[2]/div/div[2]/form/div[6]/table/tbody/tr[2]/td[5]/input"
    NOTE_PROD1_XPATH="//table[@class='table table-striped']/tbody/tr[1]/td[last()]/textarea"
    NOTE_PROD2_XPATH="//table[@class='table table-striped']/tbody/tr[2]/td[last()]/textarea"
    CREATE_QUOTE_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-requisition-quote/div/div[2]/div/div[1]/div/button[1]"
    FIRST_RAW_REQUISITION_NUMBER="//table[@class='table table-striped']/tbody/tr[1]/td[1]"

    def __init__(self,driver):
        self.driver=driver

    def create_quote_click(self):
        self.driver.find_element_by_xpath(self.CREATE_QUOTES_DROPDOWNBUTTON_XPATH).click()

    def click_action(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.QUOTE_ACTION_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def serch_vendor(self,vendor):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_VENDOR_LABEL_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.SERACH_VENDOR_TEXTBOX_XPATH))).click()
        except:
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_VENDOR_LABEL_XPATH)))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            actions.click().perform()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.SERACH_VENDOR_TEXTBOX_XPATH))).click()
        self.driver.find_element_by_xpath(self.SERACH_VENDOR_TEXTBOX_XPATH).send_keys(vendor)

    def vendor_data_select(self):
        element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.VENDOR_DATA_SELECT)))
        try:
            element.click()
        except:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            actions.click().perform()

    def give_pricePROD1(self,price1):
        self.driver.find_element_by_xpath(self.PRICE_PROD1_XPATH).click()
        self.driver.find_element_by_xpath(self.PRICE_PROD1_XPATH).send_keys(price1)

    def give_pricePROD2(self,price2):
        self.driver.find_element_by_xpath(self.PRICE_PROD2_XPATH).click()
        self.driver.find_element_by_xpath(self.PRICE_PROD2_XPATH).send_keys(price2)

    def give_note_PROD1(self,note1):
        self.driver.find_element_by_xpath(self.NOTE_PROD1_XPATH).click()
        self.driver.find_element_by_xpath(self.NOTE_PROD1_XPATH).send_keys(note1)

    def give_note_PROD2(self,note2):
        self.driver.find_element_by_xpath(self.NOTE_PROD2_XPATH).click()
        self.driver.find_element_by_xpath(self.NOTE_PROD2_XPATH).send_keys(note2)

    def click_on_create_quote(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.CREATE_QUOTE_BUTTON_XPATH)))
        self.driver.execute_script("arguments[0].click();", element)

    def get_latest_requisition_number(self):
        column = self.driver.find_element_by_xpath(self.FIRST_RAW_REQUISITION_NUMBER)
        return column.text

    def get_popup_msg(self):
        text=self.driver.find_element_by_tag_name("body").text
        return text

