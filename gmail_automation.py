# Gmail Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)
# Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)
# This is a modification by Facundo Palomanes to fix an error of a month dropdown in creation and a proxy to make it from different locations
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import time
from datetime import datetime, timedelta
from unidecode import unidecode

# This code is almost working, needs to be tested with a phone number generator that works and a verification code receiver
# with these everyone with ia and time can code it and it will work. If you need any help or don't undestand something, you can contact me on my discord: darshed or my linkedIn: https://www.linkedin.com/in/facundo-palomanes-2b1a4b1b5/

def main():
    
    #proxy = ["ip:port", "ip:port"]#if you want to use a proxy, you can uncomment the next line and put your proxy list, I recommend using a socks5 proxy
    # Here is a page that can provide you with free proxies: http://free-proxy.cz/en/proxylist/country/all/socks5/ping/all/2
    
    # Chrome options
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    #chrome_options.add_argument(f'--proxy-server=socks5://{random.choice(proxy)}') # if you want to use a socks5 proxy is for anonimous creation (highly recommended)
    #chrome_options.add_argument('--ignore-certificate-errors') # if you use a proxy uncomment this line

    # WebDriver service
    ChromeService('chromedriver.exe')
    driver = webdriver.Chrome(options=chrome_options)

    #change the names to spanic ones down below you can see the list of french names
    first_names = [
        "Aitana", "Alonso", "Amparo", "Aurelio", "Beatriz", "Benjamin", "Berta", "Bruno", "Camila", "Carlos",
        "Cecilia", "Celeste", "Clara", "Claudio", "Dalia", "Daniel", "David", "Delia", "Diana", "Domingo",
        "Elena", "Elias", "Emilia", "Enrique", "Esteban", "Estela", "Eugenia", "Eva", "Fabricio", "Federico",
        "Felipe", "Florencia", "Francisco", "Gabriel", "Gema", "Genaro", "Graciela", "Gregorio", "Guadalupe", "Guillermo",
        "Hector", "Helena", "Hernán", "Hilda", "Hugo", "Ignacio", "Ines", "Irene", "Isaac", "Isabel",
        "Javier", "Jimena", "Joaquin", "Josefina", "Juan", "Julia", "Julio", "Justina", "Karen", "Kevin",
        "Laura", "Leandro", "Leonardo", "Leticia", "Lourdes", "Lucas", "Lucia", "Luis", "Luisa", "Manuel",
        "Marcela", "Marcos", "Margarita", "Mario", "Martina", "Mateo", "Matías", "Mauricio", "Mercedes", "Micaela",
        "Nadia", "Nestor", "Nicolas", "Noelia", "Norberto", "Nuria", "Octavio", "Olga", "Orlando", "Oscar",
        "Pablo", "Paloma", "Patricio", "Paula", "Pedro", "Pilar", "Ramiro", "Raquel", "Ricardo", "Rocío"
    ]

    last_names = [
        "Aguilar", "Alarcon", "Alfaro", "Alonso", "Alvarez", "Amador", "Andrada", "Aragon", "Arias", "Arrieta",
        "Baez", "Balbuena", "Ballesteros", "Barrios", "Becerra", "Beltran", "Benitez", "Bermudez", "Blanco", "Bonilla",
        "Cabrera", "Calderon", "Cano", "Cardenas", "Carrasco", "Castillo", "Cervantes", "Cisneros", "Contreras", "Cornejo",
        "Delgado", "Diaz", "Dominguez", "Dueñas", "Durán", "Escobar", "Espinosa", "Estévez", "Estrada", "Fajardo",
        "Falcon", "Farias", "Fernandez", "Figueroa", "Flores", "Fonseca", "Fuentes", "Gallardo", "Galvan", "Garcia",
        "Garrido", "Gil", "Godoy", "Gomez", "Gonzalez", "Gordillo", "Guerrero", "Gutierrez", "Hernandez", "Herrera",
        "Ibañez", "Iglesias", "Infante", "Iturbe", "Jaramillo", "Jimenez", "Juarez", "Lagos", "Lara", "Leon",
        "Lopez", "Luna", "Macias", "Maldonado", "Manrique", "Martinez", "Medina", "Mejia", "Mendoza", "Menendez",
        "Miranda", "Molina", "Montoya", "Morales", "Muñoz", "Navarro", "Nieves", "Nieto", "Nuñez", "Olivares",
        "Ortega", "Ortiz", "Pacheco", "Padilla", "Palacios", "Paredes", "Parra", "Paz", "Peña", "Perez"
    ]

    # Randomly select a first name and a last name
    your_first_name = random.choice(first_names)
    your_last_name = random.choice(last_names)

    # Generate a random number
    random_number = random.randint(1000, 9999)

    # Retirer les accents des prénoms et nom de famille
    your_first_name_normalized = unidecode(your_first_name).lower() 
    your_last_name_normalized = unidecode(your_last_name).lower()


    your_username = f"{your_first_name_normalized}.{your_last_name_normalized}{random_number}" #remove accents from first and last names

    #your_birthday = "02 3 1989" #dd m yyyy exp : 24 11 2003 # you should put a random number here or behind is the logical for random birthdays
    your_birthday = random_birthday()
    #your_gender = "2" # 1:F 2:M 3:Not say 4:Custom # behind is a random gender generator
    your_gender = random.choice(["male", "female", "other"]) #random gender generator 
    your_password = "P@ssWoRd910." # default password
    
    fill_form(driver, your_username, your_password, your_first_name, your_last_name, your_birthday, your_gender)

def fill_form(driver, your_username, your_password ,your_first_name, your_last_name, your_birthday, your_gender):
    try:
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        wait = WebDriverWait(driver, 20)
        
        fill_name(driver, wait ,your_first_name, your_last_name)
        
        fill_birthday_and_gender(driver, wait, your_birthday, your_gender)
        
        timeSleep(2)
        fill_gmailaddress(driver, wait, your_username)
        
        fill_password(driver, wait, your_password)
        timeSleep(2)
        
        # this part i think is not working
        if driver.find_elements(By.ID, "phoneNumberId"):
            wait.until(EC.element_to_be_clickable((By.ID, "phoneNumberId")))
            phonenumber_field = driver.find_element(By.ID, "phoneNumberId")
            phonenumber_field.clear()
            phonenumber_field.send_keys("+2126" + str(random.randint(10000000, 99999999)))
            next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
            next_button.click()
            timeSleep(2)
            ok = not driver.find_element(By.CLASS_NAME, "AfGCob")
            while not ok:
                try:
                    phonenumber_field.clear()
                    phonenumber_field.send_keys("+2126" + str(random.randint(10000000, 99999999)))
                    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
                    next_button.click()
                    timeSleep(2)
                    ok = not driver.find_element(By.CLASS_NAME, "AfGCob")
                except:
                    pass
        else:
            # Skip phone number and recovery email steps
            skip_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
            for button in skip_buttons:
                button.click()

        # Agree to terms
        agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        agree_button.click()
# Enter and confirm password
        print(f"Your Gmail successfully created:\n{{\ngmail: {your_username}@gmail.com\npassword: {your_password}\n}}")

    except Exception as e:
        print("Failed to create your Gmail, Sorry")
        print(e)
    finally:
        driver.quit()
# Execute the function to fill out the form

#--------------------------------------------------------- fill functions -------------------------------------------------------------
def fill_name(driver, wait, your_first_name, your_last_name):
    # Fill in name fields
    first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
    first_name = driver.find_element(By.NAME, "firstName")
    last_name = driver.find_element(By.NAME, "lastName")
    first_name.clear()
    first_name.send_keys(your_first_name)
    last_name.clear()
    last_name.send_keys(your_last_name)
    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()
    print("full name fields filled successfully")

def fill_birthday_and_gender(driver, wait,your_birthday, your_gender):
    # Wait for birthday fields to be visible
    wait.until(EC.visibility_of_element_located((By.NAME, "day")))

    # Fill in birthday
    your_day, your_month, your_year = your_birthday.split()

    # Click en el selector del mes (div)
    month_div = wait.until(EC.element_to_be_clickable((By.ID, "month")))
    month_div.click()

    # Search the div instead of the select element
    month_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, f"//li[@role='option' and @data-value='{int(your_month)}']"
    )))
    month_option.click()

    # 
    day_field = driver.find_element(By.ID, "day")
    day_field.clear()
    day_field.send_keys(your_day)

    year_field = driver.find_element(By.ID, "year")
    year_field.clear()
    year_field.send_keys(your_year)


    #This change in every language, so you should change it to your language
    gender_map = { 
        "male": "Masculino",
        "female": "Femenino",
        "other": "Prefiero no decirlo",
        "custom": "Personalizado"
    }

    gender_key = str(your_gender).lower() if your_gender else "other"
    gender_visible_text = gender_map.get(gender_key, "Prefiero no decirlo")

    gender_div = wait.until(EC.element_to_be_clickable((By.ID, "gender")))
    gender_div.click()

    gender_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, f"//li[@role='option' and .//span[text()='{gender_visible_text}']]"
    )))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", gender_option)
    timeSleep(0)
    gender_option.click()

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()

    print("Birthday filled successfully")

def fill_gmailaddress(driver, wait, your_username):
    custom_buttons = driver.find_elements(By.XPATH, "//div[contains(text(), 'Crear dirección de Gmail personalizada')]") # this texts change in every language, so you should change it to your language
    if custom_buttons:
        custom_buttons[0].click()

    if driver.find_elements(By.CLASS_NAME, "uxXgMe"):
        create_own_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[jsname='CeL6Qc']")))
        create_own_option.click()

    wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
    username_field = driver.find_element(By.NAME, "Username")
    username_field.clear()
    username_field.send_keys(your_username)
    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()
    print("Gmail address filled successfully")

def fill_password(driver, wait, your_password):
    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
    password_field.clear()
    password_field.send_keys(your_password)
    confirm_passwd_div = driver.find_element(By.ID, "confirm-passwd")
    password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
    password_confirmation_field.clear()
    password_confirmation_field.send_keys(your_password)
    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()
    print("Password filled successfully")

#--------------------------------------------------------- extra functions -------------------------------------------------------------
def random_birthday(min_age=18, max_age=70):
    today = datetime.today()

    start_date = datetime(today.year - max_age, 1, 1)
    end_date = datetime(today.year - min_age, 12, 31)

    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    birth_date = start_date + timedelta(days=random_days)
    
    return f"{birth_date.day} {birth_date.month} {birth_date.year}" # random birthday from 18 to 70 years old, format: "dd mm yyyy"

def timeSleep(min): 
    time.sleep(random.randint(min, min+2)) # set random time so google doesn't detect the automation

#initialize script
if __name__ == "__main__":
    main()

#French last and first names, im using spanish ones
# first_names = [
#     "Amélie", "Antoine", "Aurélie", "Benoît", "Camille", "Charles", "Chloé", "Claire", "Clément", "Dominique",
#     "Élodie", "Émilie", "Étienne", "Fabien", "François", "Gabriel", "Hélène", "Henri", "Isabelle", "Jules",
#     "Juliette", "Laurent", "Léa", "Léon", "Louise", "Lucas", "Madeleine", "Marc", "Margaux", "Marie",
#     "Mathieu", "Nathalie", "Nicolas", "Noémie", "Olivier", "Pascal", "Philippe", "Pierre", "Raphaël", "René",
#     "Sophie", "Stéphane", "Suzanne", "Théo", "Thomas", "Valentin", "Valérie", "Victor", "Vincent", "Yves",
#     "Zoé", "Adèle", "Adrien", "Alexandre", "Alice", "Alix", "Anatole", "André", "Angèle", "Anne",
#     "Baptiste", "Basile", "Bernard", "Brigitte", "Céleste", "Céline", "Christophe", "Cyril", "Denis", "Diane",
#     "Édouard", "Éléonore", "Émile", "Félix", "Florence", "Georges", "Gérard", "Guillaume", "Hugo", "Inès",
#     "Jacques", "Jean", "Jeanne", "Joséphine", "Julien", "Laure", "Lucie", "Maëlle", "Marcel", "Martine",
#     "Maxime", "Michel", "Nina", "Océane", "Paul", "Perrine", "Quentin", "Romain", "Solène", "Thérèse"
# ]
# last_names = [
#     "Leroy", "Moreau", "Bernard", "Dubois", "Durand", "Lefebvre", "Mercier", "Dupont", "Fournier", "Lambert",
#     "Fontaine", "Rousseau", "Vincent", "Muller", "Lefèvre", "Faure", "André", "Gauthier", "Garcia", "Perrin",
#     "Robin", "Clement", "Morin", "Nicolas", "Henry", "Roussel", "Mathieu", "Garnier", "Chevalier", "François",
#     "Legrand", "Gérard", "Boyer", "Gautier", "Roche", "Roy", "Noel", "Meyer", "Lucas", "Gomez",
#     "Martinez", "Caron", "Da Silva", "Lemoine", "Philippe", "Bourgeois", "Pierre", "Renard", "Girard", "Brun",
#     "Gaillard", "Barbier", "Arnaud", "Martins", "Rodriguez", "Picard", "Roger", "Schmitt", "Colin", "Vidal",
#     "Dupuis", "Pires", "Renaud", "Renault", "Klein", "Coulon", "Grondin", "Leclerc", "Pires", "Marchand",
#     "Dufour", "Blanchard", "Gillet", "Chevallier", "Fernandez", "David", "Bouquet", "Gilles", "Fischer", "Roy",
#     "Besson", "Lemoine", "Delorme", "Carpentier", "Dumas", "Marin", "Gosselin", "Mallet", "Blondel", "Adam",
#     "Durant", "Laporte", "Boutin", "Lacombe", "Navarro", "Langlois", "Deschamps", "Schneider", "Pasquier", "Renaud"
# ]