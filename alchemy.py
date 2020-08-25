from sqlalchemy.interfaces import PoolListener

Base = declarative_base()

class ForeignKeysListener(PoolListener):
    def connect(self, dbapi_con, con_record):
        dbapi_con.execute('pragma foreign_keys=ON')

class DB:
    def __init__(self):
        Session = sessionmaker()
        engine = create_engine(f'sqlite:///{db_path}/.sqlite', listeners=[ForeignKeysListener()])
        engine.execute('PRAGMA encoding="UTF-8"')
        Session.configure(bind=engine)
        self.session = Session()
        Base.metadata.create_all(engine)
