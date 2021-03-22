import gspread
from oauth2client.service_account import ServiceAccountCredentials
from settings import env
from functions import ss

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(env.GOOGLE_JSON_KEY, scope)
gc = gspread.authorize(credentials)
BOOK_ID = env.BOOK_ID

book = gc.open_by_key(BOOK_ID)

sheets = ss.collect_sheets(book)

sheet = ss.get_sheet(book, 'シート1')

import_value = ss.get_cell(sheet, [1, 1])
print(import_value)

import_value = ss.get_cell(sheet, 'B1')
print(import_value)

result = ss.update_cell(sheet, 'A1', 'テスト')
print(result)

result = ss.update_cell(sheet, [1, 2], '書き換え')
print(result)
