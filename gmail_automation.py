# Gmail Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)
# Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import time
from unidecode import unidecode

# Chrome options
chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-infobars")

# WebDriver service
service = ChromeService('chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options)

french_first_names = [
    "Amélie", "Antoine", "Aurélie", "Benoît", "Camille", "Charles", "Chloé", "Claire", "Clément", "Dominique",
    "Élodie", "Émilie", "Étienne", "Fabien", "François", "Gabriel", "Hélène", "Henri", "Isabelle", "Jules",
    "Juliette", "Laurent", "Léa", "Léon", "Louise", "Lucas", "Madeleine", "Marc", "Margaux", "Marie",
    "Mathieu", "Nathalie", "Nicolas", "Noémie", "Olivier", "Pascal", "Philippe", "Pierre", "Raphaël", "René",
    "Sophie", "Stéphane", "Suzanne", "Théo", "Thomas", "Valentin", "Valérie", "Victor", "Vincent", "Yves",
    "Zoé", "Adèle", "Adrien", "Alexandre", "Alice", "Alix", "Anatole", "André", "Angèle", "Anne",
    "Baptiste", "Basile", "Bernard", "Brigitte", "Céleste", "Céline", "Christophe", "Cyril", "Denis", "Diane",
    "Édouard", "Éléonore", "Émile", "Félix", "Florence", "Georges", "Gérard", "Guillaume", "Hugo", "Inès",
    "Jacques", "Jean", "Jeanne", "Joséphine", "Julien", "Laure", "Lucie", "Maëlle", "Marcel", "Martine",
    "Maxime", "Michel", "Nina", "Océane", "Paul", "Perrine", "Quentin", "Romain", "Solène", "Thérèse"
]

french_last_names = [
    "Leroy", "Moreau", "Bernard", "Dubois", "Durand", "Lefebvre", "Mercier", "Dupont", "Fournier", "Lambert",
    "Fontaine", "Rousseau", "Vincent", "Muller", "Lefèvre", "Faure", "André", "Gauthier", "Garcia", "Perrin",
    "Robin", "Clement", "Morin", "Nicolas", "Henry", "Roussel", "Mathieu", "Garnier", "Chevalier", "François",
    "Legrand", "Gérard", "Boyer", "Gautier", "Roche", "Roy", "Noel", "Meyer", "Lucas", "Gomez",
    "Martinez", "Caron", "Da Silva", "Lemoine", "Philippe", "Bourgeois", "Pierre", "Renard", "Girard", "Brun",
    "Gaillard", "Barbier", "Arnaud", "Martins", "Rodriguez", "Picard", "Roger", "Schmitt", "Colin", "Vidal",
    "Dupuis", "Pires", "Renaud", "Renault", "Klein", "Coulon", "Grondin", "Leclerc", "Pires", "Marchand",
    "Dufour", "Blanchard", "Gillet", "Chevallier", "Fernandez", "David", "Bouquet", "Gilles", "Fischer", "Roy",
    "Besson", "Lemoine", "Delorme", "Carpentier", "Dumas", "Marin", "Gosselin", "Mallet", "Blondel", "Adam",
    "Durant", "Laporte", "Boutin", "Lacombe", "Navarro", "Langlois", "Deschamps", "Schneider", "Pasquier", "Renaud"
]

# Randomly select a first name and a last name
your_first_name = random.choice(french_first_names)
your_last_name = random.choice(french_last_names)

# Generate a random number
random_number = random.randint(1000, 9999)

# Retirer les accents des prénoms et nom de famille
your_first_name_normalized = unidecode(your_first_name).lower()
your_last_name_normalized = unidecode(your_last_name).lower()


your_username = f"{your_first_name_normalized}.{your_last_name_normalized}{random_number}"


your_birthday = "02 3 1989" #dd m yyyy exp : 24 11 2003
your_gender = "1" # 1:F 2:M 3:Not say 4:Custom
your_password = "x,nscldsj123...FDKZ"

def fill_form(driver):
    try:
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        # Fill in name fields
        first_name = driver.find_element(By.NAME, "firstName")
        last_name = driver.find_element(By.NAME, "lastName")
        first_name.clear()
        first_name.send_keys(your_first_name)
        last_name.clear()
        last_name.send_keys(your_last_name)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        # Wait for birthday fields to be visible
        wait = WebDriverWait(driver, 20)
        day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))

        # Fill in birthday
        birthday_elements = your_birthday.split()
        month_dropdown = Select(driver.find_element(By.ID, "month"))
        month_dropdown.select_by_value(birthday_elements[1])
        day_field = driver.find_element(By.ID, "day")
        day_field.clear()
        day_field.send_keys(birthday_elements[0])
        year_field = driver.find_element(By.ID, "year")
        year_field.clear()
        year_field.send_keys(birthday_elements[2])

        # Select gender
        gender_dropdown = Select(driver.find_element(By.ID, "gender"))
        gender_dropdown.select_by_value(your_gender)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        
       # Create custom email
        time.sleep(2)
        if driver.find_elements(By.ID, "selectionc4") :
            create_own_option = wait.until(EC.element_to_be_clickable((By.ID,"selectionc4") ))
            create_own_option.click()
        
        create_own_email = wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
        username_field = driver.find_element(By.NAME, "Username")
        username_field.clear()
        username_field.send_keys(your_username)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()
        
        # Enter and confirm password
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        password_field.clear()
        password_field.send_keys(your_password)
        # Locate the parent div element with the ID "confirm-passwd"
        confirm_passwd_div = driver.find_element(By.ID, "confirm-passwd")
         #Find the input field inside the parent div
        password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
        password_confirmation_field.clear()
        password_confirmation_field.send_keys(your_password)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        # Skip phone number and recovery email steps
        skip_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        for button in skip_buttons:
            button.click()

        # Agree to terms
        agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        agree_button.click()

        print(f"Your Gmail successfully created:\n{{\ngmail: {your_username}@gmail.com\npassword: {your_password}\n}}")

    except Exception as e:
        print("Failed to create your Gmail, Sorry")
        print(e)
    finally:
        driver.quit()

# Execute the function to fill out the form
fill_form(driver)
