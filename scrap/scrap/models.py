from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

from scrap import settings

DeclarativeBase = declarative_base()


class TestDB(DeclarativeBase):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)
    car = Column('car', Text())
    # author = Column('author', String(100))


def create_deals_table(engine):
    DeclarativeBase.metadata.create_all(engine)


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))
