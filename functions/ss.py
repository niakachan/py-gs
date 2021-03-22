"""
Functions for GoogleSpreadSheet
"""

def get_cell(sheet: any, cell: str):
    """Return value from Google Spread Sheet cell

    Args:
        sheet (any): Sheet model of gspread
        cell (str): Cell e.g. 'A1'

    Returns:
        any: Value of a cell
    """
    value = sheet.acell(cell).value
    return value

def get_sheets(workbook):
    """Return list of sheets in workbook

    Args:
        workbook (any): Workbook model of gspread

    Returns:
        list: Worksheets
    """
    worksheet_list = workbook.worksheets()
    return worksheet_list
