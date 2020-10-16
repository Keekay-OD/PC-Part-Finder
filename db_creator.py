from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///mymusic.db', echo=True)
Base = declarative_base()


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        """"""
        self.name = name

    def __repr__(self):
        return "<Brand: {}>".format(self.name)


class Price(Base):
    """"""
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    

    brand_id = Column(Integer, ForeignKey("brands.id"))
    brand = relationship("Brand", backref=backref(
        "prices", order_by=id))




# create tables
Base.metadata.create_all(engine)