from bs4 import BeautifulSoup
import requests
import pandas as pd


request_page = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
# request_page = requests.get('https://www.bnr.ro/files/xml/nbrfxrates2021.htm')
# print(request_page)
link = BeautifulSoup(request_page.text, 'html.parser')
# print(link)
dataset, header_list = [], []

main = link.find_all('div', attrs={'id': 'contentDiv'})
# print(main[0].find_all('table'))

for obj in main:
    # print(obj.find_all('table'))
    if len(obj.find_all('table')) > 0:
        for table_index in obj.find_all('table'):
            if len(table_index.find_all('tr')) > 0:
                header_list = [table_trs.get_text() for table_trs in table_index.find_all('th')]
                for table_row in table_index.find_all('tr'):
                    td_list = []
                    # for table_trs in table_index.find_all('th'):
                    #     header_list.append(table_trs.get_text())
                    for index, td in enumerate(table_row.find_all('td')):
                        if index == 0:
                            td_list.append(td.get_text())
                        # print(index, td)
                        elif td.get_text().strip() != '':
                            td_list.append(float(td.get_text().replace(',', '.')))
                        else:
                            td_list.append('-')
                    if len(td_list) > 0:
                        dataset.append(td_list)
                    # break

        break
# print(header_list)
# print(dataset)

df = pd.DataFrame(dataset, columns=header_list, index=range(1, 11))
print(df)
# df.to_excel('CursBnr.xlsx', header=header_list, sheet_name='CursBnr')
with pd.ExcelWriter('CursBnr_2nd_method.xlsx') as writer:
    df.to_excel(writer, index=False)
