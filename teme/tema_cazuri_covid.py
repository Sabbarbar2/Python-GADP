from bs4 import BeautifulSoup
import requests
import pandas as pd


request_page = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/')
# request_page = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
print(request_page)
link = BeautifulSoup(request_page.text, 'html.parser')
print(link)
