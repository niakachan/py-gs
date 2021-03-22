"""
Functions for GoogleSpreadSheet
"""
from typing import Union, List
from gspread.models import Worksheet, Spreadsheet


def get_cell(coordinate: List[int], sheet: Worksheet = None) -> Union[str, None]:
    value = str(sheet.cell.value(coordinate[0], coordinate[1])) if sheet else None
    return value


def update_cell(coordinate: List[int], value: Union[str, int], sheet: Worksheet = None) -> Union[dict, None]:
    old_value = get_cell(coordinate, sheet)
    sheet.update_cell(coordinate[0], coordinate[1], value) if sheet else None
    info_dict = {'Row': coordinate[0], 'Col': coordinate[1], 'Old_value': old_value, 'New_value': value} if sheet else None
    return info_dict


def get_sheets(workbook: Spreadsheet):
    worksheet_list = workbook.worksheets()
    return worksheet_list


def get_sheet(workbook: Spreadsheet, sheet_title: str):
    worksheet = workbook.worksheet(sheet_title)
    return worksheet
