from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def search_linkedin():
    driver = webdriver.Chrome(executable_path="/home/ori/WorkingDir/github/Search_linkiedin/chromedriver")
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
    while len(linkedin_urls) < 150:
        sleep(0.5)
        results = driver.find_elements_by_css_selector('div.g')
        for res in results:
            link = res.find_element_by_tag_name("a")
            linkedin_urls.append(f'{link.get_attribute("href")}\n')
            linkedin_urls = list(set(linkedin_urls))
        driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
    driver.quit()
    with open('new_links.txt', 'w') as li:
        li.writelines(linkedin_urls)


search_linkedin()
