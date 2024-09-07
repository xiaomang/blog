import os

import tornado.ioloop
import tornado.locks
import tornado.options
import tornado.web


class HomeHandler(tornado.web.RequestHandler):
    async def get(self):
        self.write({"msg": "hello world"})


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
        ]
        settings = {
            "debug": True,
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
        }
        super().__init__(handlers=handlers, **settings)


async def main():
    tornado.options.parse_command_line()

    app = Application()
    app.listen(8000)

    shutdown = tornado.locks.Event()
    await shutdown.wait()


if __name__ == "__main__":
    ioloop = tornado.ioloop.IOLoop.current()
    ioloop.run_sync(main)
