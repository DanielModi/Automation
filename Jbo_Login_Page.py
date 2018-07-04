import logging
import utilities.custom_logger as cl
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
import utilities.hash as hh

class Jbo_LoginPage:
    log = cl.customLogger(logging.DEBUG)

# Locators
    _css_username = "#md-input-1"
    _css_password = "#passwordInput"
    _css_signin_button = '.signin-button.mat-raised-button'
 #   _css_submit = 'input[type="Submit"]'
    _css_search = ".input_search"
    _css_Go_Button = ".btn_go"
    _css_Precima_label = 'a[id="dnn_dnnLOGO_hypLogo"]'
#Category selections
    _xpath_Cat_All = "//a[text()='All']"
    _xpath_Cat_insights = '//a[text()="Insights"]'
    _xpath_Cat_Assortment = '//a[text()="Assortment"]'
    _xpath_Cat_Landing_Page = '//a[text()="Landing Page"]'
    _xpath_Cat_Promotion = '//a[text()="Promotion"]'
    _xpath_Cat_Favourites = '//a[text()="Favourites"]'
    _css_Side_Bar = 'div[title="Open Secondary Sidebar"]'

    _css_List_View = 'i[id="listView"]'
    _css_Grid_View = 'i[id="gridView"]'

    _css_Sort = 'md-select[placeholder="SORT"]'
    _xpath_Ascending = '//md-option[1]'
    _xpath_Descending = '//md-option[2]'
    _xpath_Category = '//md-option[3]'

    _css_Search_Box = 'input[name="searchText"]'

    _css_Category_Dropdown = 'md-select[placeholder="CATEGORY"]'
    _xpath_Dropdown_All = '//md-option[1]'
    _xpath_Dropdown_Favourites = '//md-option[2]'
    _xpath_Dropdown_Assortment = '//md-option[3]'
    _xpath_Dropdown_Insights = '//md-option[4]'
    _xpath_Dropdown_Landing_Page = '//md-option[5]'
    _xpath_Dropdown_Promotion = '//md-option[6]'

    _css_Help_button = "div[class='mat-button-ripple mat-button-ripple-round mat-ripple']"
    _xpath_Reset_Password_Drop_down = '//span[text()="Reset password"]/parent::button'
    _xpath_Training_Button = '//span[text()="Training"]/parent::button'
    _xpath_Contact_us_Button = '//span[text()="Contact us"]/parent::button'
    _xpath_Preferences_Button = '//span[text()="Preferences"]/parent::button'
    _xpath_Log_Out = '//span[text()="Logout"]'
    _css_Advance_Analytics = 'a[title="ADVANCED ANALYTICS"]'
    _css_Price = 'a[title="PRICE"]'
    _css_report = 'md-card[class="report-container report-container-hover mat-card"]'
    _css_Ok_Thanks = 'div[class="mat-button-ripple mat-ripple"]'

    _xpath_Reset_Password_Button = '//a[text()="Reset password"]'
    _css_Email_address = 'input[placeholder="EMAIL ADDRESS"]'
    _css_Reset = 'button.signin-button'
    _xpath_Reset_back = '//i[text()="arrow_back"]'

    # Validation

    _xpath_Reports_Lable = '//div[text()="Reports"]'

    # Data
    _user_lcl_general = 'dmodi'
    _pwd_lcl_general = hh.decode('TXVtYmFpMjQ=')
    _report_name = "Alpro Jumbo Baseline Report"
    _Email_Address = "dmodi@precima.com"



    def __init__(self, selenium):
        self.driver = selenium
        self.driver.get(os.environ['base_url'])
        self.sd = SeleniumDriver(selenium)

    def enter_username(self,username):
        self.sd.sendKeys(self._user_lcl_general,self._css_username, "css")

    def enter_password(self, password):
        self.sd.sendKeys(password, self._css_password, "css")

    def click_signin(self):
        self.sd.elementClick(self._css_signin_button, "css")

    def login_LCLP(self,username,password):
        self.enter_username(username)
        sleep(2)
        self.enter_password(password)
        sleep(2)
        self.click_signin()
        sleep(2)
        self.sd.waitForElement(self._xpath_Reports_Lable, 'xpath')
        # sleep(1)
        self.sd.verify_applitool("Jumbo_Login_Verification")
        sleep(1)

    def click_precima(self):
        self.sd.elementClick(self._css_Precima_label, "css")
        sleep(5)



## Category Click

    def click_All(self):
        self.sd.elementClick(self._xpath_Cat_All, "xpath")

    def click_insights(self):
        self.sd.elementClick(self._xpath_Cat_insights, "xpath")


    def click_Assortment(self):
        self.sd.elementClick(self._xpath_Cat_Assortment, "xpath")


    def click_Landing_Page(self):
        self.sd.elementClick(self._xpath_Cat_Landing_Page, "xpath")


    def click_Promotion(self):
        self.sd.elementClick(self._xpath_Cat_Promotion, "xpath")



    def click_Favourites(self):
        self.sd.elementClick(self._xpath_Cat_Favourites, "xpath")


    def click_Side_bar(self):
        self.sd.elementClick(self._css_Side_Bar, "css")


    def Category(self):
        self.click_All()
        sleep(3)
        self.click_Side_bar()
        sleep(1)
        self.click_insights()
        sleep(1)
        self.click_Side_bar()
        sleep(1)
        self.click_Assortment()
        sleep(1)
        self.click_Side_bar()
        sleep(1)
        self.click_Landing_Page()
        sleep(1)
        self.click_Side_bar()
        sleep(1)
        self.click_Promotion()
        sleep(1)
        self.click_Side_bar()
        sleep(1)
        self.click_Favourites()
        sleep(1)
        self.sd.verify_applitool("Jumbo_Category_Verification")

 # Change view of the reports

    def click_listview(self):
        self.sd.elementClick(self._css_List_View, "css")



    def click_Gridview(self):
        self.sd.elementClick(self._css_Grid_View, "css")


    def Change_View(self):

        self.click_Gridview()
        sleep(1)
        self.click_listview()
        sleep(1)
        self.click_Gridview()
        sleep(1)


# Sorting

    def click_Sort_button(self):
        self.sd.elementClick(self._css_Sort, "css")


    def click_Sort_Ascending(self):
        self.sd.elementClick(self._xpath_Ascending, "xpath")


    def click_Sort_Descending(self):
        self.sd.elementClick(self._xpath_Descending, "xpath")


    def click_Sort_Category(self):
        self.sd.elementClick(self._xpath_Category, "xpath")


    def Sorting(self):
        self.click_Sort_button()
        sleep(1)
        self.click_Sort_Ascending()
        sleep(1)
        self.sd.verify_applitool("Jumbo_Ascending_Verification")
        sleep(1)
        self.click_Sort_button()
        sleep(1)
        self.click_Sort_Descending()
        sleep(1)
        self.sd.verify_applitool("Jumbo_Descending_Verification")
        sleep(1)
        self.click_Sort_button()
        sleep(1)
        self.click_Sort_Category()
        sleep(1)
        self.sd.verify_applitool("Jcat_Verification")
        sleep(1)

#Search box

    def click_Search_Box(self):
        self.sd.elementClick(self._css_Search_Box, "css")


    def enter_report_name(self):
        self.sd.sendKeys(self._report_name,self._css_Search_Box, "css")


    def click_report_name(self):
        self.sd.elementClick(self._css_report, "css")


    def Search(self):
        self.click_Search_Box()
        sleep(1)
        self.enter_report_name()
        sleep(1)
        self.sd.waitForElement(self._css_report, 'css')
        sleep(1)
        self.click_report_name()
        sleep(1)



# Category Dropdown list

    def click_drop_down(self):
        self.sd.elementClick(self._css_Category_Dropdown, "css")

    def click_All_Dropdown(self):
        self.sd.elementClick(self._xpath_Dropdown_All, "xpath")

    def click_Favourites_dropdown(self):
        self.sd.elementClick(self._xpath_Dropdown_Favourites, "xpath")

    def click_Insights_dropdown(self):
        self.sd.elementClick(self._xpath_Dropdown_Insights, "xpath")

    def click_Assortment_dropwown(self):
        self.sd.elementClick(self._xpath_Dropdown_Assortment, "xpath")

    def click_Landing_page_dropwown(self):
        self.sd.elementClick(self._xpath_Dropdown_Landing_Page, "xpath")


    def click_Promotion_dropwown(self):
        self.sd.elementClick(self._xpath_Dropdown_Promotion, "xpath")





    def Categoty_Dropdown_List(self):
        self.click_drop_down()
        sleep(1)
        self.click_All_Dropdown()
        sleep(1)
        self.click_drop_down()
        sleep(1)
        self.click_Favourites_dropdown()
        sleep(1)
        self.click_drop_down()
        sleep(1)
        self.click_Insights_dropdown()
        sleep(1)
        self.click_drop_down()
        sleep(1)
        self.click_Assortment_dropwown()
        sleep(1)
        self.click_drop_down()
        sleep(1)
        self.click_Landing_page_dropwown()
        sleep(1)
        self.click_drop_down()
        sleep(1)

        self.click_Promotion_dropwown()
        sleep(1)

        self.click_drop_down()
        sleep(1)
        self.click_All_Dropdown()
        sleep(1)




#Help list
    def click_Help(self):
        self.sd.elementClick(self._css_Help_button, "css")

    def click_Training(self):
        self.sd.elementClick(self._xpath_Training_Button, "xpath")


    def click_Contact_US(self):
        self.sd.elementClick(self._xpath_Contact_us_Button, "xpath")

    def click_Ok_Thanks(self):
        self.sd.elementClick(self._css_Ok_Thanks, "css")



    def Help_List(self):
        self.click_Help()
        sleep(2)
        self.click_Training()
        sleep(2)
        self.sd.verify_applitool("Jumbo_Training_Verification")
        sleep(2)
        self.click_Help()
        sleep(2)
        self.click_Contact_US()
        sleep(2)
        self.click_Ok_Thanks()
        sleep(2)



#AA Link
    def click_AA_Link(self):
        self.sd.elementClick(self._css_Advance_Analytics, "css")

        self.sd.verify_applitool("J_AA_Link_Verification")


#Custom Product List
    def click_Price_Link(self):
        self.sd.elementClick(self._css_Price, "css")

        self.sd.verify_applitool("J_Price_link_Verification")


#Logout
    def click_Log_out(self):
        self.sd.elementClick(self._xpath_Log_Out, "xpath")




#Reset password landing page

    def click_Reset_Password(self):
        self.sd.elementClick(self._xpath_Reset_Password_Button, "xpath")


    def click_Email_Address_Box(self):
        self.sd.elementClick(self._css_Email_address, "css")


    def enter_email_address(self):
        self.sd.sendKeys(self._Email_Address,self._css_Email_address, "css")


    def click_Reset(self):
        self.sd.elementClick(self._css_Reset, "css")


    def Reset_Password_From_Landing_Page(self):
        self.click_Reset_Password()
        sleep(1)
        self.click_Email_Address_Box()
        self.enter_email_address()
        self.click_Reset()
        self.sd.verify_applitool("J_Email_Sent_Verification")


# Reset password Help
    def click_Reset_Passwotd_Dropdown(self):
        self.sd.elementClick(self._xpath_Reset_Password_Drop_down, "xpath")

    def Reset_Password_From_Help(self):
        self.click_Help()
        sleep(1)
        self.click_Reset_Passwotd_Dropdown()
        sleep(1)
        self.sd.verify_applitool("J_Reset_Password_Verification")
        sleep(1)












