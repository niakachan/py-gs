from functions import ss

# スプレッドシートのURLを指定する
BOOK_URL = 'https://docs.google.com/spreadsheets/d/1sEt1V9mXT2CM7h94AgV4se3hZQlc2HzZ_ha01bzGuc0'

# URLから取得したスプレッドシートを`book`に代入
response = ss.get_book(BOOK_URL)
book = response['data']
print(response)

# `book`の中の 'Sheet1' というシートを sheet に代入
response = ss.get_sheet(book, 'Sheet1')
sheet = response['data']
print(response)

# `sheet` の内容を dictのリスト形式で取得する
response = ss.get_records(sheet)
sheet_records = response['data']
print(response)

# `sheet` の中から `10` を含むセルを検索
response = ss.get_all_cells(sheet, 10)
found_cells = response['data']
print(response)

# 検索したセルを全て`11`に更新
response = ss.update_all_cells(sheet, found_cells, 11)
updated_cells = response['data']
print(response)

# 先程値を11に置き換えたセルを全て10に戻す
response = ss.update_all_cells(sheet, updated_cells, 10)
updated_cells = response['data']
print(response)

# 行番号からセルのリストを取得する
row = 7
response = ss.get_row_cells(sheet, row)
row_cells = response['data']
print(response)

# セルのリストを値のリストに変換する
response = ss.get_cells_values(row_cells)
cells_values = response['data']
print(response)

# 列番号から1行目を無視してセルのリストを取得する
col = 4
ignore = 1
response = ss.get_col_cells(sheet, col, ignore)
col_cells = response['data']
print(response)

# セルのリストを値のリストに変換する
response = ss.get_cells_values(col_cells)
cells_values = response['data']
print(response)

# 行を1行追加
response = ss.create_row(sheet, 1)
print(response)

# 行を1行削除
response = ss.delete_row(sheet, 1)
print(response)
