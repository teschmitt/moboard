
import bottle
from moboard.routes import setup_routes


if __name__ == "__main__":

    app: bottle.Bottle = bottle.Bottle()
    bottle.TEMPLATE_PATH.append("moboard/views")

    setup_routes(app)

    try:
        bottle.run(app=app, host="localhost", port=8080, reloader=True, debug=True)

    finally:
        app.close()

