from visidata import Sheet, rotateRange


def evalmatcher(sheet, expr):
    def matcher(r):
        return sheet.evalexpr(expr, r)
    return matcher

def search_func(sheet, rows, func, reverse=False):
    for i in rotateRange(len(sheet.rows), sheet.cursorRowIndex+1, reverse=reverse):
        try:
            if func(sheet.rows[i]):
                return i
        except Exception:
            pass

Sheet.addCommand('z/', 'search-expr', 'sheet.cursorRowIndex=search_func(sheet, rows, evalmatcher(sheet, inputExpr("search by expr: "))) or status("no match")')
Sheet.addCommand('z?', 'searchr-expr', 'sheet.cursorRowIndex=search_func(sheet, rows, evalmatcher(sheet, inputExpr("search by expr: ")), reverse=True) or status("no match")')
