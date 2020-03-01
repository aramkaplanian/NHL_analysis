"""
Code by Aram Kaplanian.
Helper functions for main.py
"""


class extractor:
    import selenium

    def __init__(self, website):
        from selenium import webdriver

        self.driver = webdriver.Firefox()
        self.website = website

    def get_url(self):
        from selenium import webdriver

        self.driver = webdriver.Firefox()
        self.driver.get(self.website)

    def select_drop_downs(self, name, value):
        from selenium.webdriver.support.ui import Select

        select = Select(
            self.driver.find_element_by_class_name(name))
        select.select_by_value(value)

    def select_report(self):
        from selenium.webdriver.support.ui import Select

        select = Select(
            self.driver.find_element_by_xpath("(//select[@class='venue_select'])[2]"))
        select.select_by_value('On-Ice')

    def open_season(self):
        from selenium.webdriver.support.ui import Select

        select = self.driver.find_element_by_id('selectSeasons')
        select.click()

    def _click(self, name):
        select = self.driver.find_element_by_name(name)
        select.click()

    def click_csv(self, _css):
        from selenium.webdriver.support.ui import Select

        select = self.driver.find_element_by_css_selector(_css)
        select.click()

    def close_browser(self):
        # self.driver.close()
        self.driver.quit()

    @classmethod
    def send_to_df(cls):
        import pandas as pd

        df = pd.read_clipboard(sep=",")
        path = "C:/Users/Aram Kaplanian/nhl_notebooks/NHL_analysis/"
        df = df.to_csv(path + "team_data.csv", index=False)
