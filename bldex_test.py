import streamlit as st
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def random_sleep(min_time=0.5, max_time=2):
    time.sleep(random.uniform(min_time, max_time))

def login_to_blogdex():
    GMAIL_USER = "u.bildr.ai@gmail.com"
    PASSWORD = "gokaist2A3#"  # 실제 비밀번호로 변경하세요

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    url = "https://blogdex.space/blog-index/jo3091"
    driver.get(url)
    random_sleep()

    st.write("블덱스 페이지 로그인 중입니다")

    terms_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="terms"]'))
    )
    terms_checkbox.click()
    random_sleep()

    google_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/div[2]/button[1]'))
    )
    google_login_button.click()
    random_sleep()

    driver.switch_to.window(driver.window_handles[-1])
    random_sleep()

    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierId"]'))
    )
    email_input.send_keys(GMAIL_USER)
    email_input.send_keys(Keys.RETURN)
    random_sleep()

    password_input = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    )
    
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    random_sleep()

    driver.switch_to.window(driver.window_handles[0])
    random_sleep()

    st.write("로그인 완료!")
    return driver

st.title("블덱스 로그인 앱")

if st.button("블덱스 접속"):
    driver = login_to_blogdex()
    st.write("블덱스에 접속되었습니다.")
    st.write("브라우저를 닫으려면 이 앱을 종료하세요.")