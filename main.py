from functions import ss


BOOK_URL = 'https://docs.google.com/spreadsheets/d/1sEt1V9mXT2CM7h94AgV4se3hZQlc2HzZ_ha01bzGuc0'

book = ss.get_book(BOOK_URL)

sheets = ss.get_sheet_collection(book)
print(sheets)

sheet = ss.get_sheet(book, 0)
print(sheet)

response = ss.create_sheet(book, 'NewSheet', [1000, 1000])
print(response)

new_sheet = response.get('sheet')

response = ss.delete_sheet(book, new_sheet)
print(response)

old_title = sheet.title

response = ss.update_sheet_title(book, sheet, 'シート2')
print(response)

response = ss.update_sheet_title(book, sheet, old_title)
print(response)

import_value = ss.get_cell(sheet, [1, 1])
print(import_value)

import_value = ss.get_cell(sheet, 'B1')
print(import_value)

result = ss.update_cell(sheet, 'A1', 'TESTING')
print(result)

result = ss.update_cell(sheet, [1, 1], 'going fine')
print(result)
