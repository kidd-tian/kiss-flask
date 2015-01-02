# -*- coding: utf-8 -*-
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from ..extensions import db


class Home(db.Model):
    __tablename__ = 'home'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __init__(self, name):
        self.name = name
