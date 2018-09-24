import tornado.ioloop
from tornado.web import Application
from handlers.Main import HomePageHandler


def make_app():
    return Application([
        (r"/home", HomePageHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
