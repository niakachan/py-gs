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


def get_sheet_titles(workbook: Spreadsheet) -> list:
    """Googleスプレッドシート内にあるシートのタイトルリストを取得する

    Args:
        workbook (Spreadsheet): gspread で定義されているSpreadsheetモデル

    Returns:
        list: スプレッドシート内の全てのシートのタイトルリスト
    """
    sheets = get_sheet_collection(workbook)
    sheet_titles = [sheet.title for sheet in sheets]
    return sheet_titles


def create_sheet(workbook: Spreadsheet, title: str, size: list) -> dict:
    """新しいシートを作成する

    Args:
        workbook (Spreadsheet): gspread で定義されているSpreadsheetモデル
        title (str): 作成するシートのタイトル
        size (list): 作成するシートのサイズ[row, col]
        e.g. [10, 20]
    Returns:
        dict: 作成結果
        e.g. {'action:': create_sheet, 'result': 'Success', 'message': 'Created a sheet: {sheet title}', 'data': sheet}
    """
    action = 'create_sheet'
    sheet_titles = get_sheet_titles(workbook)
    if title not in sheet_titles and len(size) == 2:
        workbook.add_worksheet(title=title, rows=size[0], cols=size[1])
        new_sheet = get_sheet(workbook, title)
        response = {'action:': action, 'result': 'Success', 'message': 'Created a sheet: {}'.format(title), 'data': new_sheet}
    elif title in sheet_titles:
        sheet = get_sheet(workbook, title)
        response = {'action:': action, 'result': 'Failure', 'message': 'The sheet already exists.', 'data': sheet}
    elif len(size) != 2:
        response = {'action:': action, 'result': 'Failure', 'message': 'The size specification is wrong.', 'data': None}
    else:
        response = {'action:': action, 'result': 'Failure', 'message': 'Undefined error', 'data': None}
    return response


def delete_sheet(workbook: Spreadsheet, sheet: Union[Worksheet, None]) -> dict:
    """シートを削除する

    Args:
        workbook (Spreadsheet): gspread で定義されているSpreadsheetモデル
        sheet (Union[Worksheet, None]): gspread で定義されているWorksheetモデル

    Returns:
        dict: 削除結果
        e.g. {'action:': action, 'result': 'Success', 'message': 'Deleted a sheet: {sheet title}, 'data': workbook}
    """
    action = 'delete_sheet'
    if sheet:
        workbook.del_worksheet(sheet)
        response = {'action:': action, 'result': 'Success', 'message': 'Deleted a sheet: {}'.format(sheet.title), 'data': workbook}
    else:
        response = {'action:': action, 'result': 'Failure', 'message': 'The sheet does not exist.', 'data': workbook}
    return response


def get_sheet(workbook: Spreadsheet, sheet_identifier: Union[str, int]) -> Union[Worksheet, None]:
    """シートをWorksheetとして取得する。

    Args:
        workbook (Spreadsheet): gspread で定義されているSpreadsheetモデル
        sheet_identifier (Union[str, int]): シート識別子 strの場合はシートの名前で、intの場合は何番目のシートかを指定して取得する
        e.g. 'シート1' or 0

    Returns:
        Union[Worksheet, None]: gspread で定義されているWorksheetモデル
    """
    if type(sheet_identifier) == str:
        worksheet = workbook.worksheet(sheet_identifier)
    elif type(sheet_identifier) == int:
        worksheet = workbook.get_worksheet(sheet_identifier)
    else:
        worksheet = None
    return worksheet


def update_sheet_title(workbook: Spreadsheet, sheet: Union[Worksheet, None], title) -> dict:
    """シートのタイトルを変更する

    Args:
        workbook (Spreadsheet): gspread で定義されているSpreadsheetモデル
        sheet (Union[Worksheet, None]): gspread で定義されているWorksheetモデル
        title ([type]): 新しくつけるタイトル

    Returns:
        dict: 更新結果
        e.g. {'action:': action, 'result': 'Success', 'message': 'Updated sheet title {old_title} to {new_title}, 'data': sheet}
    """
    action = 'update_sheet_title'
    sheet_titles = get_sheet_titles(workbook)
    if title not in sheet_titles:
        if sheet:
            old_title = sheet.title
            if old_title != title:
                sheet.update_title(title)
                new_title = sheet.title
                response = {'action:': action, 'result': 'Success', 'message': 'Updated sheet title {} to {}'.format(old_title, new_title), 'data': sheet}
            else:
                response = {'action:': action, 'result': 'Failure', 'message': 'Same title as before.', 'data': sheet}
        else:
            response = {'action:': action, 'result': 'Failure', 'message': 'The sheet does not exist.', 'data': None}
    else:
        response = {'action:': action, 'result': 'Failure', 'message': 'The sheet already exists.', 'data': sheet}
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
        Union[dict, None]: 更新結果
        e.g. {'action:': action, 'result': 'Success', 'message': 'Updated value {old_value} to {new_value}', 'data': new_value}
    """
    action = 'update_cell'
    if sheet:
        old_value = get_cell(sheet, coordinate)
        if old_value != value:
            if type(coordinate) == str:
                old_value = get_cell(sheet, coordinate) or 'None'
                sheet.update_acell(coordinate, value)
                new_value = get_cell(sheet, coordinate)
                response = {'action:': action, 'result': 'Success', 'message': 'Updated value {} to {}'.format(old_value, new_value), 'data': new_value}
            elif type(coordinate) == list and len(coordinate) == 2:
                old_value = get_cell(sheet, coordinate) or 'None'
                sheet.update_cell(coordinate[0], coordinate[1], value)
                new_value = get_cell(sheet, coordinate)
                response = {'action:': action, 'result': 'Success', 'message': 'Updated value {} to {}'.format(old_value, new_value), 'data': new_value}
            else:
                response = {'action:': action, 'result': 'Failure', 'message': 'Wrong argument.', 'data': old_value}
        else:
            response = {'action:': action, 'result': 'Failure', 'message': 'Same value as before.', 'data': old_value}
    else:
        response = response = {'action:': action, 'result': 'Failure', 'message': 'The sheet does not exist.', 'data': None}
    return response


def get_range(sheet: Union[Worksheet, None], range: str) -> list:
    """シートの範囲を指定して1次元配列を取得する

    Args:
        sheet (Union[Worksheet, None]): gspread で定義されているWorksheetモデル
        range (str): 範囲 e.g. 'A1:B10'

    Returns:
        list: 範囲に含まれる値の1次元配列
    """
    if sheet:
        response = sheet.range(range)
    else:
        response = []
    return response


def get_row_list(sheet: Union[Worksheet, None], row: int) -> list:
    """行番号から値のリストを取得する

    Args:
        sheet (Union[Worksheet, None]): gspread で定義されているWorksheetモデル
        row (int): 行番号

    Returns:
        list: 行の値の1次元配列
    """
    if sheet:
        response = sheet.row_values(row)
    else:
        response = []
    return response


def get_col_list(sheet: Union[Worksheet, None], col: int) -> list:
    """列番号から値のリストを取得する

    Args:
        sheet (Union[Worksheet, None]): gspread で定義されているWorksheetモデル
        row (int): 列番号

    Returns:
        list: 行の値の1次元配列
    """
    if sheet:
        response = sheet.col_values(col)
    else:
        response = []
    return response


def get_cell_list(sheet: Union[Worksheet, None]) -> list:
    """シートから全ての値の多次元リストを取得する

    Args:
        sheet (Union[Worksheet, None]): gspread で定義されているWorksheetモデル

    Returns:
        list: 行の値の多次元配列
    """
    if sheet:
        response = sheet.get_all_values()
    else:
        response = []
    return response


def get_cell_dict(sheet: Union[Worksheet, None]) -> list:
    """シートから全ての値を辞書形式のリストで取得する

    Args:
        sheet (Union[Worksheet, None]): gspread で定義されているWorksheetモデル

    Returns:
        list[dict]: 辞書形式のリスト
    """
    if sheet:
        response = sheet.get_all_records(empty2zero=False, head=1, default_blank='')
    else:
        response = [{}]
    return response


def search_cell(sheet: Union[Worksheet, None], string: str) -> dict:
    """シート内から特定の値のセルを取得する

    Args:
        sheet (Union[Worksheet, None]): [description]
        string (str): [description]

    Returns:
        dict: 検索結果
        e.g. {'action:': action, 'result': 'Success', 'message': 'Contents of the cell have been retrieved. content: {content} row: {row} col: {col}, 'data': cell}
    """
    action = 'search_cell'
    if sheet:
        try:
            cell = sheet.find(string)
            content = str(cell.value)
            row = str(cell.row)
            col = str(cell.col)
            response = {'action:': action, 'result': 'Success', 'message': 'Contents of the cell have been retrieved. content: {} row: {} col: {}'.format(content, row, col), 'data': cell}
        except Exception:
            response = {'action:': action, 'result': 'Failure', 'message': 'Data not found', 'data': None}
    else:
        response = {'action:': action, 'result': 'Failure', 'message': 'The sheet does not exist.', 'data': None}
    return response
