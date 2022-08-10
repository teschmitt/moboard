from bottle import static_file

from moboard.controllers import get_img, get_js, get_css, index


def setup_routes(app):
    app.route("/img/<filename>", "GET", get_img)
    app.route("/js/<filename>", "GET", get_js)
    app.route("/css/<filename>", "GET", get_css)
    app.route(
        "/favicon.ico",
        "GET",
        static_file("favicon.ico", root="moboard/assets/img"),
    )
    app.route(
        "/favicon.png",
        "GET",
        static_file("favicon.ico", root="moboard/assets/img"),
    )
    app.route("/hello/<name>", "GET", index)
