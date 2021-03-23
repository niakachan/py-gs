from functions import ss

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

