import os
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.locks
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        
        handlers = [
            (r"/", HomeHandler),
            (r"/echo/([^/]+)", EchoHandler),
        ]

        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)

class HomeHandler(tornado.web.RequestHandler):
    async def get(self):
        self.write('Hello World!')

class EchoHandler(tornado.web.RequestHandler):
    async def get(self, cmd):
        self.write(cmd)

async def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    shutdown_event = tornado.locks.Event()
    await shutdown_event.wait()

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
