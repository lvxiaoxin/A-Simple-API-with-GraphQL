# -*- coding: utf-8 -*-
"""
@version: 
@time: 2018/9/12
@author: lvxiaoxin
@software: PyCharm
@file: databases
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

__author__ = 'lvxin'

engine = create_engine('sqlite://thrones.db', convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
