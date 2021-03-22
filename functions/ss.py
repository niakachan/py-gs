"""
GoogleSpreadSheet の値操作関連
"""
from typing import Union
from gspread.models import Worksheet, Spreadsheet


def collect_sheets(workbook: Spreadsheet):
    worksheet_list = workbook.worksheets()
    return worksheet_list


def get_sheet(workbook: Spreadsheet, sheet_identifier: Union[str, int]) -> Union[Worksheet, None]:
    """シートをWorksheetとして取得する。

    Args:
        workbook (Spreadsheet): gspread で定義されているSpreadsheetモデル
        sheet_identifier (Union[str, int]): シート識別子 strの場合はシートの名前で、intの場合は何番目のシートかを指定して取得する
        e.g. 'シート1' or 0

    Returns:
        Union[Worksheet, None]: [description]
    """
    if type(sheet_identifier) == str:
        worksheet = workbook.worksheet(sheet_identifier)
    elif type(sheet_identifier) == int:
        worksheet = workbook.get_worksheet(sheet_identifier)
    else:
        worksheet = None
    return worksheet


def get_cell(sheet: Union[Worksheet, None], coordinate: Union[list, str]) -> Union[str, None]:
    """スプレッドシートのセルから値を取得する

    Args:
        sheet (Worksheet, optional): gspread で定義されているWorksheetモデル
        coordinate (Union[list, str]): 取得対象セルの座標指定 ラベルでも座標でも指定可能
        e.g. 'A1' or [1,1]

    Returns:
        Union[str, None]: 取得した値
    """
    if sheet:
        if type(coordinate) == str:
            value = str(sheet.acell(coordinate).value)
        elif type(coordinate) == list:
            value = str(sheet.cell(coordinate[0], coordinate[1]).value)
        else:
            value = None
    else:
        value = None
    return value


def update_cell(sheet: Union[Worksheet, None], coordinate: Union[list, str], value: Union[str, int]) -> Union[dict, None]:
    """スプレッドシートのセルの内容を更新する

    Args:
        sheet (Worksheet, optional): gspread で定義されているWorksheetモデル
        coordinate (Union[list, str]): 取得対象セルの座標 ラベルでも座標でも指定可能
        e.g. 'A1' or [1,1]
        value (Union[str, int]): 新しくセルに入れる値

    Returns:
        Union[dict, None]: 更新結果の辞書
    """
    if sheet:
        old_value = get_cell(sheet, coordinate)
        if type(coordinate) == str:
            sheet.update_acell(coordinate, value)
            response = {'Label': coordinate, 'Old_value': old_value, 'New_value': value}
        elif type(coordinate) == list:
            sheet.update_cell(coordinate[0], coordinate[1], value)
            response = {'Row': coordinate[0], 'Col': coordinate[1], 'Old_value': old_value, 'New_value': value}
        else:
            response = None
    else:
        response = None
    return response
