from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


driver = webdriver.Chrome()


driver.get("https://localhost")


time.sleep(2)


form_elements = driver.find_elements(By.CSS_SELECTOR, "input, select, textarea")


for element in form_elements:
    tag_name = element.tag_name
    input_type = element.get_attribute("type")
    
    try:

        if tag_name == "input":
            if input_type in ["text", "password"]:
                element.send_keys("Sample text") 
            elif input_type == "email":
                element.send_keys("example@example.com")  
            elif input_type == "number":
                element.send_keys(random.randint(1, 100))  
            elif input_type == "checkbox":
                if not element.is_selected():
                    element.click() 
            elif input_type == "radio":
                element.click() 
        elif tag_name == "select":
            options = element.find_elements(By.TAG_NAME, "option")
            random.choice(options).click()  
        elif tag_name == "textarea":
            element.send_keys("Sample text in textarea")
    
    except Exception as e:
        print(f"Could not interact with the element: {e}")


driver.find_element(By.ID, "submit-button").click()

time.sleep(5)


driver.quit()
