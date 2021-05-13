import config
from selenium import webdriver
import pandas as pd


def get_best_movie_oscar():
    url = 'https://tr.wikipedia.org/wiki/En_%C4%B0yi_Film_Akademi_%C3%96d%C3%BCl%C3%BC'
    driver = webdriver.Chrome(executable_path=config.chrome_driver_path)
    driver.get(url)
    columns = [i.text for i in driver.find_element_by_xpath(
        '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[1]').find_elements_by_tag_name('th')]
    rows = driver.find_elements_by_xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr')[1:]
    my_data = pd.DataFrame(columns=columns)
    for index, row in enumerate(rows):
        cells = [i.text for i in row.find_elements_by_tag_name('td')]
        cells[3] = cells[3].split("\n")
        cells[4] = cells[4].split("\n")
        my_data.loc[index] = cells
        print(cells)
    return my_data


if __name__ == '__main__':
    oscar_data = get_best_movie_oscar()
    oscar_data.to_excel(config.csv_save_path,index=False,encoding='utf-8')
