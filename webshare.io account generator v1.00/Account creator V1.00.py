import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import numpy as np
import io

# Password Generator Function
def generate_password():
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special_characters = '!@#&'

    password = random.choice(alphabets).upper() + ''.join(random.choice(alphabets + digits + special_characters) for _ in range(7))
    return password

# Email Generator Function
def generate_emails(names=[]):
    email_list = []
    for nm in names:
        email_list.append(
            nm.strip().split('\n')[0] + '{}{}'.format(np.random.randint(1, 99), '@gmail.com')
        )
    return email_list

# Load names list
names_list = io.open("names.txt", "r").readlines()

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\bobby\Downloads\webshare.io account generator v1.00\chromedriver-win64\chromedriver.exe")

# Navigate to the registration page
driver.get("https://proxy2.webshare.io/register")

# Fill in the email and password fields
email_field = driver.find_element(By.ID, "email-input")
emails = generate_emails(names_list)
email = random.choice(emails)
email_field.send_keys(email)

password_field = driver.find_element(By.ID, ":R2l579nmj6:")
password = generate_password()
password_field.send_keys(password)

# Click on the "SIGN UP" button
sign_up_button = driver.find_element(By.XPATH, "//button[contains(@data-testid, 'signup-button')]")
sign_up_button.click()

# Wait for a few seconds
time.sleep(5)

# Click on the "Let's get started" button
get_started_button = driver.find_element(By.XPATH, "//button[contains(text(), \"Let's get started\")]")
get_started_button.click()

# Wait for a few seconds
time.sleep(5)

# Click on the "DOWNLOAD PROXY LIST" button
download_button = driver.find_element(By.XPATH, "//a[contains(@data-testid, 'download-button')]")
download_button.click()

# Wait for a few seconds
time.sleep(5)

# Close the browser window
driver.quit()
Creator-BobbyTatum-Made-With-Chat-GPT-3.5
