"""
GoogleSpreadSheet の値操作関連
"""
import gspread
from gspread.models import Worksheet, Spreadsheet
from oauth2client.service_account import ServiceAccountCredentials
from typing import Union
from settings import env

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(env.GOOGLE_JSON_KEY, scope)
client = gspread.authorize(credentials)


def get_book(book_identifier: str) -> Spreadsheet:
    """Googleスプレッドシートを取得する

    Args:
        book_identifier (str): シートのURLまたはキー

    Returns:
        Spreadsheet: gspread で定義されているSpreadsheetモデル
    """
    if 'http' in book_identifier:
        workbook = client.open_by_url(book_identifier)
    else:
        workbook = client.open_by_key(book_identifier)
    return workbook


def get_sheet_collection(workbook: Spreadsheet) -> list:
    """Googleスプレッドシート内にあるシートのリストを取得する

    Args:
        workbook (Spreadsheet): gspread で定義されているSpreadsheetモデル

    Returns:
        list: スプレッドシート内の全てのシートのリスト
    """
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


def update_sheet_title(sheet: Union[Worksheet, None], title) -> dict:
    if sheet:
        old_title = sheet.title
        if old_title != title:
            sheet.update_title(title)
            new_title = sheet.title
            response = {'result': 'Success', 'old_title': old_title, 'new_title': new_title}
        else:
            response = {'result': 'Same title as before.', 'old_title': old_title}
    else:
        response = {'result': 'The sheet does not exist.'}
    return response


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
        elif type(coordinate) == list and len(coordinate) == 2:
            value = str(sheet.cell(coordinate[0], coordinate[1]).value)
        else:
            value = None
    else:
        value = None
    return value


def update_cell(sheet: Union[Worksheet, None], coordinate: Union[list, str], value: Union[str, int]) -> dict:
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
        if old_value != value:
            if type(coordinate) == str:
                sheet.update_acell(coordinate, value)
                new_value = get_cell(sheet, coordinate)
                response = {'result': 'Success', 'label': coordinate, 'old_value': old_value, 'new_value': new_value}
            elif type(coordinate) == list and len(coordinate) == 2:
                sheet.update_cell(coordinate[0], coordinate[1], value)
                new_value = get_cell(sheet, coordinate)
                response = {'result': 'Success', 'row': coordinate[0], 'col': coordinate[1], 'old_value': old_value, 'new_value': new_value}
            else:
                response = {'result': 'Wrong argument.', 'old_value': old_value}
        else:
            response = {'result': 'Same value as before.', 'old_value': old_value}
    else:
        response = response = {'result': 'The sheet does not exist.'}
    return response
