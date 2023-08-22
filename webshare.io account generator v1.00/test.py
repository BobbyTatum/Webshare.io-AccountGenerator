import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import numpy as np
import io
import os
import pydub
import urllib
from speech_recognition import Recognizer, AudioFile

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
driver = webdriver.Chrome(executable_path=r"C:\\Users\\bobby\\OneDrive\\Desktop\\chromedriver-win64\\chromedriver.exe")

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

# Solve reCAPTCHA audio challenge
frames = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[-1])
driver.find_element(By.ID, "recaptcha-audio-button").click()
sleep(2)
driver.switch_to.default_content()
frames = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[-1])
sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/button").click()
sleep(2)

try:
    src = driver.find_element(By.ID, "audio-source").get_attribute("src")
    urllib.request.urlretrieve(src, "audio.mp3")
    sound = pydub.AudioSegment.from_mp3("audio.mp3").export("audio.wav", format="wav")

    recognizer = Recognizer()
    recaptcha_audio = AudioFile("audio.wav")

    with recaptcha_audio as source:
        audio = recognizer.record(source)

    text = recognizer.recognize_google(audio, language="de-DE")

    inputfield = driver.find_element(By.ID, "audio-response")
    inputfield.send_keys(text.lower())
    inputfield.send_keys(Keys.ENTER)

    # Wait for a few seconds
    time.sleep(5)

    # Click on the download proxy button
    download_button = driver.find_element(By.LINK_TEXT, "DOWNLOAD PROXY LIST")
    download_button.click()

    # Wait for a few seconds
    time.sleep(5)

    print("Captcha solved and proxies downloaded successfully.")
except:
    print("Captcha solving failed.")

# Close the browser window
driver.quit()
