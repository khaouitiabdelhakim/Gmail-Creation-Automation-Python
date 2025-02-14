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

french_first_names = ["Amélie", "Antoine", "Aurélie", "Benoît", "Camille", "Charles", "Chloé", "Claire", "Clément", "Dominique", "Élodie", "Émilie", "Étienne", "Fabien", "François", "Gabriel", "Hélène", "Henri", "Isabelle", "Jules", "Juliette", "Laurent", "Léa", "Léon", "Louise", "Lucas", "Madeleine", "Marc", "Margaux", "Marie", "Mathieu", "Nathalie", "Nicolas", "Noémie", "Olivier", "Pascal", "Philippe", "Pierre", "Raphaël", "René", "Sophie", "Stéphane", "Suzanne", "Théo", "Thomas", "Valentin", "Valérie", "Victor", "Vincent", "Yves", "Zoé", "Adèle", "Adrien", "Alexandre", "Alice", "Alix", "Anatole", "André", "Angèle", "Anne", "Baptiste", "Basile", "Bernard", "Brigitte", "Céleste", "Céline", "Christophe", "Cyril", "Denis", "Diane", "Édouard", "Éléonore", "Émile", "Félix", "Florence", "Georges", "Gérard", "Guillaume", "Hugo", "Inès", "Jacques", "Jean", "Jeanne", "Joséphine", "Julien", "Laure", "Lucie", "Maëlle", "Marcel", "Martine", "Maxime", "Michel", "Nina", "Océane", "Paul", "Perrine", "Quentin", "Romain", "Solène", "Thérèse"]
french_last_names = ["Leroy", "Moreau", "Bernard", "Dubois", "Durand", "Lefebvre", "Mercier", "Dupont", "Fournier", "Lambert", "Fontaine", "Rousseau", "Vincent", "Muller", "Lefèvre", "Faure", "André", "Gauthier", "Garcia", "Perrin", "Robin", "Clement", "Morin", "Nicolas", "Henry", "Roussel", "Mathieu", "Garnier", "Chevalier", "François", "Legrand", "Gérard", "Boyer", "Gautier", "Roche", "Roy", "Noel", "Meyer", "Lucas", "Gomez", "Martinez", "Caron", "Da Silva", "Lemoine", "Philippe", "Bourgeois", "Pierre", "Renard", "Girard", "Brun", "Gaillard", "Barbier", "Arnaud", "Martins", "Rodriguez", "Picard", "Roger", "Schmitt", "Colin", "Vidal", "Dupuis", "Pires", "Renaud", "Renault", "Klein", "Coulon", "Grondin", "Leclerc", "Pires", "Marchand", "Dufour", "Blanchard", "Gillet", "Chevallier", "Fernandez", "David", "Bouquet", "Gilles", "Fischer", "Roy", "Besson", "Lemoine", "Delorme", "Carpentier", "Dumas", "Marin", "Gosselin", "Mallet", "Blondel", "Adam", "Durant", "Laporte", "Boutin", "Lacombe", "Navarro", "Langlois", "Deschamps", "Schneider", "Pasquier", "Renaud"]

def generate_username(first_name, last_name):
    first_name_normalized = unidecode(first_name).lower()
    last_name_normalized = unidecode(last_name).lower()
    random_number = random.randint(1000, 9999)
    return f"{first_name_normalized}.{last_name_normalized}{random_number}"

def fill_form(driver):
    try:
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        wait = WebDriverWait(driver, 20)

        # Fill in name fields
        first_name = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        last_name = driver.find_element(By.NAME, "lastName")
        first_name.send_keys(random.choice(french_first_names))
        last_name.send_keys(random.choice(french_last_names))
        driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe").click()

        # Fill in birthday and gender
        day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))
        birthday_elements = "02 3 1989".split()
        Select(driver.find_element(By.ID, "month")).select_by_value(birthday_elements[1])
        driver.find_element(By.ID, "day").send_keys(birthday_elements[0])
        driver.find_element(By.ID, "year").send_keys(birthday_elements[2])
        Select(driver.find_element(By.ID, "gender")).select_by_value("1")
        driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe").click()

        # Create custom email
        time.sleep(2)
        if driver.find_elements(By.CLASS_NAME, "uxXgMe"):
            driver.find_element(By.CSS_SELECTOR, "[jsname='CeL6Qc']").click()
        username_field = wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
        username_field.send_keys(generate_username(random.choice(french_first_names), random.choice(french_last_names)))
        driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe").click()

        # Enter and confirm password
        password = "x,nscldsj123...FDKZ"
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        password_field.send_keys(password)
        driver.find_element(By.NAME, "PasswdAgain").send_keys(password)
        driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe").click()

        # Handle phone number if needed
        time.sleep(2)
        if driver.find_elements(By.ID, "phoneNumberId"):
            phonenumber_field = wait.until(EC.element_to_be_clickable((By.ID, "phoneNumberId")))
            phonenumber_field.send_keys("+2126" + str(random.randint(10000000, 99999999)))
            driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
            time.sleep(2)
            while driver.find_elements(By.CLASS_NAME, "AfGCob"):
                phonenumber_field.clear()
                phonenumber_field.send_keys("+2126" + str(random.randint(10000000, 99999999)))
                driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
                time.sleep(2)
        else:
            for button in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d"))):
                button.click()

        # Agree to terms
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d"))).click()

        print(f"Your Gmail successfully created:\n{{\ngmail: {username_field.get_attribute('value')}@gmail.com\npassword: {password}\n}}")

    except Exception as e:
        print("Failed to create your Gmail, Sorry")
        print(e)
    finally:
        driver.quit()

fill_form(driver)