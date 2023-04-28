import requests
from bs4 import BeautifulSoup
import pandas as pd

for data in range(1, 6):
    url = f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{data}-martie-ora-13-00-2/"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("div", class_="entry-content")


    rows = table.find_all("tr")

    header_row = rows[0]
    header_columns = header_row.find_all("td")
    column_names = [column.get_text(strip=True) for column in header_columns]

    desired_columns = ["Județ", "Număr de cazuri confirmate(total)"]
    column_indexes = []
    for column in desired_columns:
        if column in column_names:
            column_indexes.append(column_names.index(column))
        else:
            print(f"Column '{column}' not found.")

    for row in rows[1:]:
        columns = row.find_all("td")

        data = [columns[index].get_text(strip=True) if index < len(columns) else "" for index in column_indexes]
        print(data)
