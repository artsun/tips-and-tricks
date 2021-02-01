from contextlib import contextmanager


def dict_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    '''
    В SQLite нет встроенной фабрики для строк в виде dict.
    '''
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@contextmanager
def conn_context(db_path: str):
    '''
    В SQLite нет контекстного менеджера для работы с соединениями.
    :param db_path: путь до базы данных
    '''
    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    yield conn
    conn.close()
