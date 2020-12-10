from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import Urls


    drive = webdriver.Chrome(executable_path="PATH_TO_FILE_WEBDRIVER")

    drive.get('https:www.google.com')
    search_query = drive.find_element_by_name('q').send_keys('site:linkedin.com/in/ AND "I\'m hiring" AND "Israel"')
    search_query = drive.find_element_by_name('q').send_keys(Keys.RETURN)
    sleep(2)

    linkedin_urls = drive.find_elements_by_tag_name('cite')
    linkedin_urls = drive.find_elements_by_class_name('iUh30')
    linkedin_urls = [url.text for url in linkedin_urls]
    print(len(linkedin_urls))
    print(linkedin_urls)
    # driver.get('https://www.linkedin.com/login')
    # print(driver.title)
    # username = driver.find_element_by_id('username').send_keys('email@gmail.com')
    # password = driver.find_element_by_id('password').send_keys('pessword')
    # log_in_button = driver.find_element_by_xpath('//*[@type="submit"]').click()

    if linkedin_urls:
        Urls.add_url(url.text)
    else:
        print("Try again")

    drive.quit()

search_linkedin()