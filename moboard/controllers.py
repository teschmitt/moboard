import asyncio
from typing import Coroutine

from bottle import static_file, template

from moboard.models import Newsgroup


def run_async(func: Coroutine):
    loop = asyncio.new_event_loop()
    return loop.run_until_complete(func)


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


async def get_all_newsgroups():
    return [g["name"] for g in (await Newsgroup.all().values("name"))]


def show_newsgroups():
    return template(
        "newsgroups.tpl", newsgroups=run_async(get_all_newsgroups())
    )
