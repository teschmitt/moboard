import bottle

from config import config
from moboard.routes import setup_routes


if __name__ == "__main__":

    app: bottle.Bottle = bottle.Bottle()
    bottle.TEMPLATE_PATH.append("moboard/views")

    setup_routes(app)

    try:
        bottle.run(
            app=app,
            host=config["host_address"],
            port=config["host_port"],
            reloader=True,
            debug=True,
        )

    finally:
        app.close()
