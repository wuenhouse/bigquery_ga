import os, sys
from datetime import datetime, timedelta, date
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def gsheet(key):
    sheet = client.open_by_key(key).get_worksheet(3)
    titles = ('欄位1', '欄位2')
    sheet.insert_row(titles, 1)
    data = [('wendell', 'like'), ('damon', 'like')]
    for x in data:
        sheet.append_row(x)

def read_sheet(key, sheet_index):
    sheet = client.open_by_key(key).get_worksheet(sheet_index)
    return sheet

if __name__ == '__main__':
    try:
        d = datetime.strptime(sys.argv[1], '%Y%m%d')
    except:
        os._exit(0)

    # google sheet key_id
    key_id = "11IkV75BZA5esQdWC1Bgm6_6Yvu8LtWeG7Xf_94ybtaU"

    # gsheet(key_id)
    scopes = ["https://spreadsheets.google.com/feeds"]

    # download from google service
    json_key_path = "/Users/huangyankai/Downloads/gs_key.json"

    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scopes)
    client = gspread.authorize(credentials)

    sh = read_sheet(key_id, 0)
    # first_column = sh.col_values(1)
    # print(first_column)
    list_of_lists = sh.get_all_values()
    for r in list_of_lists:
        print(r)
