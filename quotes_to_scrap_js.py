import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

class Website:
    def __init__(self):
        self.MAIN_URL = "http://quotes.toscrape.com/js/"
        self.COLUMNS = ["Author", "Quote"]
        self.quotes_array = [[],[]]

    def open_main_page(self):
        self.driver = Firefox()
        #self.driver.minimize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.MAIN_URL)

    def write_quotes_array(self, pages=1):
        #log_file = open("./log.csv", "w")

        for page in range(0, pages):
            quotes_cards = self.driver.find_elements(By.CSS_SELECTOR, ".quote")

            print("PAGINA {} escrita!".format(page+1))
            
            for index, quote_card in enumerate(quotes_cards):
                self.quotes_array[0].append(quote_card.find_element(By.CSS_SELECTOR, ".author").text)
                self.quotes_array[1].append(quote_card.find_element(By.CSS_SELECTOR, ".text").text.replace("“", "\"").replace("”", "\""))
            
            if(page < pages-1):
                self.driver.find_element(By.CSS_SELECTOR, ".next a").click()

        #log_file.close()

    def print_quotes_array(self):
        page = 1
        for index in range(0, len(self.quotes_array[0])):
            print("{}# {}-{}".format(index+1, self.quotes_array[0][index], self.quotes_array[1][index]))
            
            if((index)%10 == 0):
                print("Pagina {}".format(page))
                page += 1
    
    def export_quotes_array(self):
        FILE_NAME = "Quotes_To_Scrap.csv"

        file = open(FILE_NAME, "w")

        for index in range(0, len(self.COLUMNS)):
            if(index < len(self.COLUMNS)-1):
                file.write("{},".format(self.COLUMNS[index]))
            else:
                file.write("{}\n".format(self.COLUMNS[index]))
        
        for index in range(0, len(self.quotes_array[0])):
            file.write("{},{}\n".format(self.quotes_array[0][index], self.quotes_array[1][index]))

    def end_session(self):
        self.driver.quit()
    
    #def update_quote_dict(quotes_array, author, quote):