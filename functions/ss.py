"""
Functions for GoogleSpreadSheet
"""

from typing import Union

def get_cell(sheet: any, cell: Union[str, int]):
    value = str(sheet.acell(cell).value)
    return value

def get_sheets(workbook):
    worksheet_list = workbook.worksheets()
    return worksheet_list

def get_sheet(workbook, sheet_title: str):
    worksheet = workbook.worksheet(sheet_title)
    return worksheet
