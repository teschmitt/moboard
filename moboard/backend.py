import nntplib

from config import config


class HackedNNTP(nntplib.NNTP):
    def current(self, limit):
        resp, lines = self._longcmdstring(f"CURRENT {limit}")
        return resp, [line.split("\t") for line in lines]


server = HackedNNTP(host=config["server_address"], port=config["server_port"])


def get_all_newsgroups():
    response = server.list()
    return [group.group for group in response[1]]


def get_all_articles(newsgroup_name):
    articles = []
    group_response, num_articles, first, last, _ = server.group(newsgroup_name)
    if "211" in group_response:
        try:
            over_response, overviews = server.over((first, last))
            if "224" in over_response:
                articles = [article[1] for article in overviews]
        except nntplib.NNTPTemporaryError:
            # some error fetching articles from group
            pass
    return articles


def get_single_article(message_id):
    _, info = server.article(message_id)
    article = {"body": ""}
    body_started = False

    for line in info.lines:
        line_decode = line.decode()
        if not body_started and ":" in line_decode:
            field, value = map(
                lambda s: s.strip(), line_decode.split(sep=":", maxsplit=1)
            )
            article[field.lower()] = value
        elif len(line_decode) < 1:
            # empty line between header and body
            body_started = True
            continue
        elif body_started:
            article["body"] += line_decode

    return article


def get_current_articles(limit):
    return [
        {
            "subject": field[1],
            "from": field[2],
            "date": field[3],
            "message-id": field[4],
            "newsgroup_name": field[5]
        }
        for field in server.current(limit)[1]
    ]
