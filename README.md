# moboard

A minimalistic web-based news client for the
[moNNT.py Usenet server](https://github.com/teschmitt/moNNT.py)

## Getting Started

Download this repo and then run
```shell
$ poetry run python main.py
```

## Configuration

All configuration options can be found in `pyproject.toml`. A quick rundown:

- `server_address`: address the server can be found under
- `server_port`: port of the server
- `group`: either a group name carried by the server or `"all"`. If a group name is supplied, `moboard` will only show an article list of this group on the home page, if `"all"` is given, the list of newsgroups carried by the server will be displayed.
- `load_articles`: number of articles to load on the overview pages


## Dependencies

mboard uses [bottle.py](https://bottlepy.org) and the
[toml](https://pypi.org/project/toml/) package, 
that's it.

Styling is done with a minified artifact of the excellent 
[Pico.css Minimal CSS Framework for semantic HTML](https://github.com/picocss/pico).