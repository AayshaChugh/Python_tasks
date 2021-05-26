import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) # chrome window open
 
driver.get("https://linkedin.com/login")
try:
    driver.maximize_window() # chrome maximize
    sleep(5)
    if(driver.current_url=="https://linkedin.com/login" or "linkedin.com/login"): # checking id loggedin or not
        username=driver.find_element_by_id("username") # username element fetch
        username.send_keys("maillikhio") # mail submitted
        password=driver.find_element_by_id("password")
        password.send_keys("*********")
        submit_btn=driver.find_element_by_class_name("btn__primary--large") # submit button ko find kiya
        submit_btn.click()
    driver.get("https://www.linkedin.com/mynetwork/invitation-manager/") # connection reuest display
    sleep(2) # data load
    ex_cept=driver.find_elements_by_class_name("invitation-card__action-btn") # list fetch where invitation card action button hga
    for btn in ex_cept:
        a=btn.get_attribut("aria-label")
        if a[0:6]=="Accept":
            btn.click()
            print("ho gya")
        else:
            print("bht hi bdiya nhi ho pana")
    print("khatam program")
except Exception as e:
    print("error aa ra h")
