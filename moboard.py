import asyncio
from asyncio import AbstractEventLoop

from tortoise import run_async
import bottle
from moboard.db import db_init
from moboard.routes import setup_routes


def main():
    print("HAHAHAHAH")


if __name__ == "__main__":
    run_async(db_init())

    app: bottle.Bottle = bottle.Bottle()
    bottle.TEMPLATE_PATH.append("moboard/views")
    loop: AbstractEventLoop = asyncio.new_event_loop()

    setup_routes(app)

    try:

        bottle.run(app=app, host="localhost", port=8080, reloader=True, debug=True)

    finally:
        app.close()
        loop.stop()
        loop.close()

