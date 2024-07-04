from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login_instagram(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(username)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)

def report_profile(driver, victim_username):
    driver.get(f"https://www.instagram.com/{victim_username}/")
    time.sleep(2)

    dots_button = driver.find_element(By.XPATH, "//button[contains(@class, 'wpO6b')]")
    dots_button.click()
    time.sleep(2)

    report_button = driver.find_element(By.XPATH, "//button[text()='Report User']")
    report_button.click()
    time.sleep(2)

    spam_option = driver.find_element(By.XPATH, "//button[text()='Spam']")
    spam_option.click()
    time.sleep(2)

    confirm_button = driver.find_element(By.XPATH, "//button[text()='Report']")
    confirm_button.click()
    time.sleep(2)

def report_accounts(victim_username, accounts_file):
    accounts = []
    with open(accounts_file, 'r') as file:
        for line in file:
            username, password = line.strip().split(':')
            accounts.append({"username": username, "password": password})

    driver = webdriver.Chrome()

    for account in accounts:
        login_instagram(driver, account["username"], account["password"])
        report_profile(driver, victim_username)
        driver.delete_all_cookies()

    driver.quit()
