from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.youtube.com')
search_box = driver.find_element_by_xpath(
    '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
search_box.send_keys('na tum jaano na hum shirley setia remix ')

search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_button.click()
song = driver.find_element_by_xpath(
    '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img')
song.click()
