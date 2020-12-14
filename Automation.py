from selenium import webdriver
from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import os
from Messages import get_msg_from_file


def search_linkedin():
    driver = webdriver.Chrome(executable_path="WEBDRIVER_PATH")
    driver.maximize_window()
    wait = WebDriverWait(driver, 40)
    driver.get('https:www.google.com')
    driver.find_element_by_name('q').send_keys('site:linkedin.com/in/ AND "KEYWORD" AND "LOCATION"')
    driver.find_element_by_name('q').send_keys(Keys.RETURN)
    visiteid_links = list()
    if (os.path.exists('visiteid_list.txt')):
        with open('visiteid_list.txt') as exlude:
            for link in exlude.readlines():
                visiteid_links.append(link.rstrip('\n'))
    linkedin_urls = list()
    while len(linkedin_urls) < 150:
        sleep(0.5)
        results = driver.find_elements_by_css_selector('div.g')
        for res in results:
            link = res.find_element_by_tag_name("a")
            pure_link = link.get_attribute("href")
            if pure_link not in visiteid_links:
                linkedin_urls.append(f'{pure_link}\n')
                linkedin_urls = list(set(linkedin_urls))
        driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
    with open('new_links.txt', 'w') as li:
        li.writelines(linkedin_urls)
    driver.get('https://www.linkedin.com/login')
    driver.find_element_by_id('username').send_keys('EMAIL@gmail.com')
    driver.find_element_by_id('password').send_keys('PESSWORD')
    driver.find_element_by_xpath('//*[@type="submit"]').click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[contains(@class, 'search-global-typeahead')]")))

    with open('new_links.txt') as file:
        lines = file.readlines()
        for line in lines:
            try:
                driver.get(line.rstrip())
                driver.find_element_by_xpath("//*[contains(@aria-label, 'Connect')]").click()
                with_note = driver.find_element_by_xpath("//*[contains(@aria-label, 'Add a note')]")
                message = get_msg_from_file('FILES_PATH')
                sleep(1)
                with_note.click()
                try:
                    if driver.find_element_by_id('email'):
                        continue
                except common.exceptions.NoSuchElementException:
                    pass
                driver.find_element_by_xpath("//*[contains(@id, 'custom-message')]").send_keys(message)
                driver.find_element_by_xpath("//*[contains(@aria-label, 'Send now')]").click()
            except common.exceptions.NoSuchElementException:
                pass
            with open('visiteid_list.txt', 'w+') as done:
                done.write(f'{line}\n')
    os.remove('new_links.txt')

    driver.quit()


search_linkedin()
