from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def search_linkedin():
    driver = webdriver.Chrome(executable_path="PATH_TO_FILE_WEBDRIVER")
    driver.maximize_window()
    # driver.get('https://www.linkedin.com/login')
    # print(driver.title)
    # username = driver.find_element_by_id('username').send_keys('email@gmail.com')
    # password = driver.find_element_by_id('password').send_keys('pessword')
    # log_in_button = driver.find_element_by_xpath('//*[@type="submit"]').click()

    driver.get('https:www.google.com')
    driver.find_element_by_name('q').send_keys('site:linkedin.com/in/ AND "I\'m hiring" AND "Israel"')
    driver.find_element_by_name('q').send_keys(Keys.RETURN)
    linkedin_urls = list()
    for i in range(10):
        sleep(2)
        results = driver.find_elements_by_css_selector('div.g')
        for res in results:
            link = res.find_element_by_tag_name("a")
            linkedin_urls.append(f'{link.get_attribute("href")}\n')
        driver.find_element_by_xpath("//*[contains(local-name(), 'span') and contains(text(), 'Next')]").click()
        print(len(linkedin_urls))
        print(linkedin_urls)
    driver.quit()
    with open('new_links.txt', 'w') as li:
        li.writelines(linkedin_urls)


search_linkedin()
