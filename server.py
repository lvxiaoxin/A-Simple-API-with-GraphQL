# -*- coding: utf-8 -*-
"""
@version: 
@time: 2018/9/12
@author: lvxiaoxin
@software: PyCharm
@file: server
"""

from flask import Flask
from flask_graphql import GraphQLView

from databases import db_session
from schema import schema

__author__ = 'lvxin'

app = Flask(__name__)

app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
