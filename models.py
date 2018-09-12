# -*- coding: utf-8 -*-
"""
@version: 
@time: 2018/9/12
@author: lvxiaoxin
@software: PyCharm
@file: models
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from databases import Base

__author__ = 'lvxin'


class Families(Base):
    __tablename__ = 'families'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    rank = Column(Integer)


class Members(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    gender = Column(String(50))
    families_id = Column(Integer, ForeignKey('families.id'))
    families = relationship(Families, backref=backref('employee', uselist=True, cascade='delete,all'))
