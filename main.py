import gspread
import json
from settings import env
from oauth2client.service_account import ServiceAccountCredentials
from functions import ss

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(env.GOOGLE_JSON_KEY, scope)
gc = gspread.authorize(credentials)
SPREADSHEET_KEY = env.SPREADSHEET_KEY

#共有設定したスプレッドシートのシート1を開く
sheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

import_value = ss.get_cell(sheet, 'A1')

print(import_value)

# #A1セルの値に100加算した値をB1セルに表示させる
# export_value = import_value+100
# sheet.update_cell(1,2, export_value)
