from data.configuration import HOST, DB, USER, PASSWD
import sqlalchemy
from sqlalchemy.orm import sessionmaker


class ShipflowDB:
    def __init__(self):
        self._engine = sqlalchemy.create_engine(f'postgresql://{USER}:{PASSWD}@{HOST}/{DB}')

        self._metadata = sqlalchemy.MetaData()
        self._metadata.reflect(bind=self._engine)
        self._session_maker = sessionmaker(bind=self._engine)

    def __repr__(self):
        return f"<ShipflowDB engine={self._engine}>"

    def get_session(self):
        return self._session_maker()

    def get_table_model(self, table_name):
        table_model = sqlalchemy.Table(table_name,
                                       self._metadata,
                                       autoload=True)

        return table_model