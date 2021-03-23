from functions import ss
import time

# スプレッドシートのURLを指定する
BOOK_URL = 'https://docs.google.com/spreadsheets/d/1sEt1V9mXT2CM7h94AgV4se3hZQlc2HzZ_ha01bzGuc0'

# URLから取得したスプレッドシートを`book`に代入
book = ss.get_book(BOOK_URL)

# `book`の中の 'Sheet1' というシートを sheet に代入
sheet = ss.get_sheet(book, 'Sheet1')
print(sheet)

# `sheet` の内容を dict形式で取得する
sheet_dict = ss.get_dict(sheet)
print(sheet_dict)

# `sheet` の中から `10` を含むセルを検索
response = ss.search_all_cells(sheet, 10)
found_cells = response['data']
print(response)

# 検索したセルを全て`11`に更新
response = ss.update_all_cells(sheet, found_cells, 11)
updated_cells = response['data']
print(response)

# 3秒待つ
time.sleep(3)

# 先程値を11に置き換えたセルを全て10に戻す
response = ss.update_all_cells(sheet, updated_cells, 10)
updated_cells = response['data']
print(response)
