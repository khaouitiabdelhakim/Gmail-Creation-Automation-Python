# Gmail Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

#chrome_options = ChromeOptions()
#chrome_options.add_argument("--disable-infobars")  # Optional: Disable info bars

service = ChromeService('chromedriver.exe')
driver = webdriver.Chrome(service=service) #, options=chrome_options)


# your data
your_first_name = "Gamal"
your_last_name = "DoeLy"
your_username = "gamadoe1445pro" # gama1445pro@gmail.com // make sure to be unique
your_birthday = "02 3 1999" #dd m yyyy exp : 24 11 2003
your_gender = "1" # 1:F 2:M 3:Not say 4:Custom
your_password = "x,nscldsj123...FDKZ"

try:
    driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

    first_name = driver.find_element(By.NAME, "firstName")
    last_name = driver.find_element(By.NAME, "lastName")

    first_name.clear()
    first_name.send_keys(your_first_name)

    last_name.clear()
    last_name.send_keys(your_last_name)

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()

    wait = WebDriverWait(driver, 20)
    day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))

    birthday_elements = your_birthday.split()

    month_dropdown = Select(driver.find_element(By.ID, "month"))
    month_dropdown.select_by_value(birthday_elements[1])

    day_field = driver.find_element(By.ID, "day")
    day_field.clear()
    day_field.send_keys(birthday_elements[0])

    year_field = driver.find_element(By.ID, "year")
    year_field.clear()
    year_field.send_keys(birthday_elements[2])

    gender_dropdown = Select(driver.find_element(By.ID, "gender"))
    gender_dropdown.select_by_value(your_gender)

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()

    create_own_option = wait.until(EC.element_to_be_clickable((By.ID, "selectionc2")))
    create_own_option.click()

    create_own_email = wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
    username_field = driver.find_element(By.NAME, "Username")
    username_field.clear()
    username_field.send_keys(your_username)

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()

    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
    password_field.clear()
    password_field.send_keys(your_password)

    password_confirmation_field = driver.find_element(By.NAME, "PasswdAgain")
    password_confirmation_field.clear()
    password_confirmation_field.send_keys(your_password)

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()

    # Skip add phone number
    skip_button_is_visible = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
    skip_button = driver.find_element(By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")
    skip_button.click()

    # Skip add recovery email
    skip_button_is_visible = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
    skip_button = driver.find_element(By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")
    skip_button.click()

    next_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "VfPpkd-LgbsSe")))
    next_button.click()

    # Agree on Google's privacies
    agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
    agree_button.click()

    # Close the browser window at the end of your automation
    driver.quit()

    print("Your Gmail successfully created:\n{\ngmail: " + your_username + "@gmail.com\npassword: " + your_password + "\n}")


except Exception as e:
    # Close the browser window in case of failure
    driver.quit()
    print("Failed to create your Gmail, Sorry")
    print(e)
