from tornado.web import RequestHandler
from libs.database import ShipflowDB
from data.configuration import TEMPLATE_DIR

class HomePageHandler(RequestHandler):
    def get(self):
        db = ShipflowDB()

        db_session = db.get_session()
        ship_model = db.get_table_model('ships')

        all_ships = db_session.query(ship_model).all()

        self.render(f"{TEMPLATE_DIR}/all_ships.html", all_ships=all_ships)