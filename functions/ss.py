"""
Functions for GoogleSpreadSheet
"""

def get_cell(sheet: any, cell: str):
    """Get value from Google Spread Sheet cell

    Args:
        sheet (any): Sheet model of gspread
        cell (str): Cell e.g. 'A1'

    Returns:
        any: Value of a cell
    """
    value = sheet.acell(cell).value
    return value
