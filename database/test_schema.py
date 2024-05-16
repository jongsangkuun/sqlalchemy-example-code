from sqlalchemy import Column, Integer, String
from database import Base


class SearchOneTable(Base):
    __tablename__ = "search_one_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class SearchManyTable(Base):
    __tablename__ = "search_many_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class InsertOneTable(Base):
    __tablename__ = "insert_one_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class InsertManyTable(Base):
    __tablename__ = "insert_many_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class UpdateOneTable(Base):
    __tablename__ = "update_one_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class UpdateManyTable(Base):
    __tablename__ = "update_many_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class DeleteOneTable(Base):
    __tablename__ = "delete_one_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class DeleteManyTable(Base):
    __tablename__ = "delete_many_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
