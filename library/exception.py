class BookNotFound(Exception):
    """요청한 책이 없는 경우"""
    pass


class BookHasNoBorrowHistory(Exception):
    """요청한 책이 없는 경우"""
    pass
