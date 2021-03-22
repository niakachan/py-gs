from functions import ss


BOOK_ID = '1sEt1V9mXT2CM7h94AgV4se3hZQlc2HzZ_ha01bzGuc0'
BOOK_URL = 'https://docs.google.com/spreadsheets/d/1sEt1V9mXT2CM7h94AgV4se3hZQlc2HzZ_ha01bzGuc0'

book = ss.get_book(BOOK_URL)

sheets = ss.collect_sheets(book)

sheet = ss.get_sheet(book, 'シート1')

import_value = ss.get_cell(sheet, [1, 1])
print(import_value)

import_value = ss.get_cell(sheet, 'B1')
print(import_value)

result = ss.update_cell(sheet, 'A1', 'TEST')
print(result)

result = ss.update_cell(sheet, [1, 2], 'WRIGHTING')
print(result)
