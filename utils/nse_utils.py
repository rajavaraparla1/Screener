
import requests
from constants import constants, tickers, urls
from bs4 import BeautifulSoup
import pandas as pd


def get_option_chain(ticker,expiry):
    subst_url=urls.option_chain_base_url.format(ticker,expiry)
    page = requests.get(subst_url)
    if(page.status_code == constants.REQUEST_SUCCESS_CODE):
        soup = BeautifulSoup(page.content,'html.parser')
        table_it=soup.find_all(class_="opttbldata")
        table_cls_1 = soup.find_all(id="octable")
        col_list=[]
        for mytable in table_cls_1:
            table_head = mytable.find('thead')
            try:
                rows=table_head.find_all('tr')
                for tr in rows:
                    cols = tr.find_all('th')
                    for th in cols:
                        er=th.text
                        ee=er.encode('utf8')
                        ee = str(ee, 'utf-8')
                        col_list.append(ee)

            except:
                print ("no head")
        col_list_final = [e for e in col_list if e not in ('CALLS','PUTS','Chart','\xc2\xa0','\xa0')]
        print (col_list_final)
        table_cls_2 = soup.find(id="octable")
        all_trs = table_cls_2.find_all('tr')
        req_row = table_cls_2.find_all('tr')

        new_table = pd.DataFrame(index=range(0, len(req_row) - 3), columns=col_list_final)

        row_marker = 0

        for row_number, tr_nos in enumerate(req_row):

            # This ensures that we use only the rows with values
            if row_number <= 1 or row_number == len(req_row) - 1:
                continue

            td_columns = tr_nos.find_all('td')

            # This removes the graphs columns
            select_cols = td_columns[1:22]
            cols_horizontal = range(0, len(select_cols))

            for nu, column in enumerate(select_cols):
                utf_string = column.get_text()
                utf_string = utf_string.strip('\n\r\t": ')

                tr = utf_string.encode('utf-8')
                tr = str(tr, 'utf-8')
                tr = tr.replace(',', '')
                new_table.iloc[row_marker, [nu]] = tr

            row_marker += 1

        if len(req_row) > 0:
            print(new_table)
            return True
            return new_table

        else :
            return None
