import random

import flask

mad = flask.Flask(__name__)


@mad.route("/")
def index():
    night = random.random
    return flask.render_template('index.html', index=index)






@mad.route("/site2")
def roses():
    return flask.render_template('roses.html', roses=roses)






@mad.route("/site3")
def nenorm():
    return flask.render_template('nenorm.html', nenorm=nenorm)





@mad.route("/site4")
def ahahah():
    return flask.render_template('ahahah.html', ahahah=ahahah)


if __name__ == "__main__":
    mad.run()
