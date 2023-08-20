from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from my_info import *


chrome_driver_path = Service("C:\development\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3690152289&f_AL=true&geoId=102241850&keywords=python%20developer&location=Victoria%2C%20Australia&refresh=true")
# time.sleep(1000)

# wait = WebDriverWait(driver, 10)
signin = driver.find_element(By.LINK_TEXT,"Sign in")
signin.click()

input_email = driver.find_element(By.ID, "username")
input_email.send_keys(my_email)

input_password = driver.find_element(By.ID, "password")
input_password.send_keys(my_password)
input_password.send_keys(Keys.ENTER)

time.sleep(5)
'''
# save_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]')
# save_button.click()
'''
all_jobs_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")
print(all_jobs_list)
for job in all_jobs_list:
    print(job)
    job.click()
    print("after job click...")
    time.sleep(5)
    easy_apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
    easy_apply_button.click()

    try:
        submit_button = driver.find_element(By.CSS_SELECTOR, "#artdeco-button button")
        if submit_button.get_attribute("aria-label") == "Submit Application":
            phone_no = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
            if phone_no.get_attribute("value") == "":
                phone_no.send_keys(my_mobile)

            submit_button.click()
            time.sleep(5)
            print("application has been completed. ")
        else:
            print("close pop up windows")
            driver.find_element(By.CSS_SELECTOR, "#artdeco-modal__dismiss svg").click()
            time.sleep(5)



    except NoSuchElementException:
        print("No application button, skipped.")

time.sleep(5)
driver.quit()


