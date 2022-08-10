from bottle import static_file

from moboard.controllers import (
    get_img,
    get_js,
    get_css,
    show_index,
    favicon,
    show_newsgroups,
    show_articles,
    show_single_article,
)


def setup_routes(app):
    """
    Sets up all routes for the moboard application
    :param app: Bottle app object to set up routes on
    :return:  None
    """

    # Static assets and test routes
    app.route("/img/<filename>", "GET", get_img)
    app.route("/js/<filename>", "GET", get_js)
    app.route("/css/<filename>", "GET", get_css)
    app.route("/favicon.ico", "GET", favicon)

    # Newsgroup routes
    app.route("/", "GET", show_index)
    app.route("/newsgroups", "GET", show_newsgroups)
    app.route("/newsgroups/<newsgroup_name>", "GET", show_articles)
    app.route("/article/<message_id>", "GET", show_single_article)
