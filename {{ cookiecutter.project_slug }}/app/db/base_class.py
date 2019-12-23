from sqlalchemy.ext.declarative import declared_attr, declarative_base


class CustomBase(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)