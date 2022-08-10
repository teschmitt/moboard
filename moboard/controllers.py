from bottle import static_file, template

from moboard.backend import (
    get_all_articles,
    get_all_newsgroups,
    get_single_article,
    get_current_articles,
)


def index(name):
    return template("index.tpl", name=name)
    # return template("<b>Hello {{name}}</b>!", name=name)


def get_img(filename):
    return static_file(filename, root="moboard/assets/img")


def get_js(filename):
    return static_file(filename, root="moboard/assets/js")


def get_css(filename):
    return static_file(filename, root="moboard/assets/css")


def favicon():
    return static_file("favicon.ico", root="moboard/assets/img")


def show_articles(newsgroup_name):
    return template(
        "articles.tpl",
        newsgroup_name=newsgroup_name,
        articles=get_all_articles(newsgroup_name),
    )


def show_newsgroups():
    return template("newsgroups.tpl", newsgroups=get_all_newsgroups())


def show_single_article(message_id):
    return template(
        "single_article.tpl",
        article=get_single_article(message_id),
    )


def show_index():
    return template(
        "index.tpl",
        articles=get_current_articles(10),
    )
