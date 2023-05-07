import requests
from bs4 import BeautifulSoup
import pandas as pd


urls = [
    "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/",
    "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00-2/",
    "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00-2/",
    "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-2/",
]


def extract_table_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    data = []
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        row_data = [cell.text.strip() for cell in cells]
        data.append(row_data)

    return data


data_first_link = extract_table_data(urls[0])


header_row = data_first_link[0]
total_cases_index = header_row.index("Număr de cazuri confirmate(total)")


final_dataframe = pd.DataFrame(data_first_link[1:], columns=header_row).iloc[:, [0, 1, total_cases_index]]


for i, url in enumerate(urls):
    date_column = f"{i+1:02}.03"
    data_other_link = extract_table_data(url)
    other_link_dataframe = pd.DataFrame(data_other_link[1:], columns=header_row)
    final_dataframe[date_column] = other_link_dataframe["Număr de cazuri confirmate(total)"]


final_dataframe.to_excel("Tema_mai_webscraping.xlsx", index=False)
