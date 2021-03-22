import gspread
from oauth2client.service_account import ServiceAccountCredentials
from settings import env
from functions import ss

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(env.GOOGLE_JSON_KEY, scope)
gc = gspread.authorize(credentials)
BOOK_ID = env.BOOK_ID

book = gc.open_by_key(BOOK_ID)
print(book)

sheets = ss.get_sheets(book)

sheet = book.sheet1

import_value = ss.get_cell([1, 1], sheet)

print(import_value)

result = ss.update_cell([1, 2], value='test', sheet=sheet)

print(result)
