#from bs4 import BeautifulSoup
import quotes_to_scrap_js

website = quotes_to_scrap_js.Website()

pages = int(input("Quantas páginas deseja captar?\n(10 frases por página):"))

website.open_main_page()
website.write_quotes_array(pages=pages)
website.print_quotes_array()
website.export_quotes_array()
website.end_session()