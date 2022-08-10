from bottle import static_file, template


def index(name):
    return template("index.tpl", name=name)
    # return template("<b>Hello {{name}}</b>!", name=name)


def get_img(filename):
    return static_file(filename, root="moboard/assets/img")


def get_js(filename):
    return static_file(filename, root="moboard/assets/js")


def get_css(filename):
    return static_file(filename, root="moboard/assets/css")
