from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

try:

    driver.get("https://localhost")


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "frmprice")))


    driver.execute_script("document.getElementsByName('check_email')[0].value='invalid';")
    driver.execute_script("document.getElementsByName('act')[0].value='add';")
    driver.execute_script("document.getElementsByName('newpq')[0].value='';")
    driver.execute_script("document.getElementsByName('txtSourceId')[0].value='1';")
    driver.execute_script("document.getElementsByName('qsVal')[0].value='q';")
    driver.execute_script("document.getElementsByName('getJobId')[0].value='';")


    driver.find_element(By.NAME, "clientEmail").send_keys("your_email@example.com")
    driver.find_element(By.NAME, "clientFName").send_keys("YourFirstName")
    driver.find_element(By.NAME, "clientLName").send_keys("YourLastName")


    doc_type_group_id = driver.find_element(By.NAME, "docTypeGroupId")
    doc_type_group_id.send_keys("1") 


    doc_type_id = driver.find_element(By.NAME, "docTypeId")
    doc_type_id.send_keys("56")


    driver.find_element(By.NAME, "clientTitle").send_keys("Document Title")
    

    driver.find_element(By.NAME, "wordcount").send_keys("10000")


    driver.find_element(By.ID, "instructions").send_keys("Additional instructions.")


    driver.find_element(By.NAME, "phoneNo1").send_keys("1234567890")


    best_time_call = driver.find_element(By.NAME, "rdBestTimeToCall")
    best_time_call.send_keys("Morning")


    timezone = driver.find_element(By.NAME, "timezone")
    timezone.send_keys("-8") 


    country = driver.find_element(By.NAME, "country")
    country.send_keys("1") 


    driver.find_element(By.ID, "submit-button").click()


    time.sleep(5)

finally:

    driver.quit()
