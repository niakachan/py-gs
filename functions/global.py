def print_error(e):
    """Error内容を出力します。
    """
    print(type(e))
    print(e.args)
    print(e)
    print('TraceBack：' + e.traceback.format_exc())
    return e
