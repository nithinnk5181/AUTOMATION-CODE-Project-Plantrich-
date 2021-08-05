#   pytest -v -s --html=Reports/test_login_report.html --self-contained-html Testcases/test_login.py --browser Firefox
#  pytest -v -s Testcases/test_login.py --browser Firefox
#  pytest -v -s Testcases/test_login.py --browser Chrome

import pytest
from PageObjects.LoginPage import Login
from Utilities.customLogger import LogGen
from Utilities.readproperties import ReadConfig
import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASEURL=ReadConfig.getBaseuRL()

class Test_001_Login():

    logger=LogGen.loggen()#log save
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=1)
    def test_loginSuccess(self,setup):
        self.logger.info("*************Test_001_Login*************")
        self.logger.info("*************Verifying_login_Success*************")
        self.driver = setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)  # classObject
        self.lp.login()
        ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL)) #Wait for the next page to load
            assert True
            self.driver.close()
            self.logger.info("*************Login_Successfull_test_is_passed*************")
        except:
            #To take the Screenshote
            date_stamp = str(datetime.datetime.now()).split('.')[0]
            filename="testlogin "+date_stamp + ".png"
            self.driver.save_screenshot("Screenshotes/"+filename)
            self.logger.error("*************Login_Successfull_test_is_Failed*************")
            assert False


class Test_002_Login():

    logger = LogGen.loggen()  # log save

    @pytest.mark.run(order=2)
    @pytest.mark.regression
    def test_loginfailed(self,setup):
        self.driver = setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)  # classObject
        self.lp.Fake_login("ABCD", "1234")
        ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home"
        try:
            WebDriverWait(self.driver, 5).until(EC.url_to_be(ExpectedURL)) #Wait for the next page to load
            self.logger.error("*************Login_Successfull_test_is_Failed*************")
            # To take the Screenshote
            date_stamp = str(datetime.datetime.now()).split('.')[0]
            filename = "testlogin " + date_stamp + ".png"
            self.driver.save_screenshot("Screenshotes/" + filename)
            assert False
        except:
            self.driver.close()
            self.logger.info("*************Login_Successfull_test_is_passed*************")
            assert True

    @pytest.mark.run(order=3)
    @pytest.mark.regression
    def test_loginfailedwithNullValue(self,setup):
        self.driver = setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)  # classObject
        self.lp.Fake_login("", "")
        ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home"
        try:
            WebDriverWait(self.driver, 5).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            self.logger.error("*************Login_Successfull_test_is_Failed*************")
            # To take the Screenshote
            date_stamp = str(datetime.datetime.now()).split('.')[0]
            filename = "testlogin " + date_stamp + ".png"
            self.driver.save_screenshot("Screenshotes/" + filename)
            assert False
        except:
            self.driver.close()
            self.logger.info("*************Login_Successfull_test_is_passed*************")
            assert True

class Test_003_Login():

    logger = LogGen.loggen()  # log save

    @pytest.mark.skip
    @pytest.mark.regression
    @pytest.mark.run(order=4)
    @pytest.mark.skip
    def test_VendorloginSuccess(self,setup):
        self.driver = setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)  # classObject
        self.lp.vendorlogin()
        ExpectedURL = "#fill here "
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            assert True
            self.driver.close()
            self.logger.info("*************Login_Successfull_test_is_passed*************")
        except:
            # To take the Screenshote
            date_stamp = str(datetime.datetime.now()).split('.')[0]
            filename = "testlogin " + date_stamp + ".png"
            self.driver.save_screenshot("Screenshotes/" + filename)
            self.logger.error("*************Login_Successfull_test_is_Failed*************")
            assert False


class Test_004_Login():

    logger = LogGen.loggen()  # log save

    @pytest.mark.run(order=5)
    @pytest.mark.regression
    def test_ForgotpasswordPresend(self,setup):
        self.driver = setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)  # classObject
        try:
            self.lp.Forgetpassword()
            self.driver.close()
            assert True
        except NoSuchElementException:
            #To take the Screenshote
            date_stamp = str(datetime.datetime.now()).split('.')[0]
            filename="testlogin "+date_stamp + ".png"
            self.driver.save_screenshot("Screenshotes/"+filename)
            assert False
