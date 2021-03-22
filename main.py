from functions import ss


BOOK_URL = 'https://docs.google.com/spreadsheets/d/1sEt1V9mXT2CM7h94AgV4se3hZQlc2HzZ_ha01bzGuc0'

book = ss.get_book(BOOK_URL)

sheets = ss.collect_sheets(book)

sheet = ss.get_sheet(book, 0)

response = ss.update_sheet_title(sheet, '新しいタイトル')
print(response)
old_title = response.get('old_title')
response = ss.update_sheet_title(sheet, old_title)
print(response)

import_value = ss.get_cell(sheet, [1, 1])
print(import_value)

import_value = ss.get_cell(sheet, 'B1')
print(import_value)

result = ss.update_cell(sheet, 'A1', 'TEST')
print(result)

result = ss.update_cell(sheet, [1, 2], 'going')
print(result)
