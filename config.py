from selenium import webdriver

chrome_driver_path = 'D:/chromedriver.exe'

option = webdriver.ChromeOptions()
option.add_argument('headless')


csv_save_path = 'D:/oscar_data.xlsx'
