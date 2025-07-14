from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    JSON
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Chat(Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True)
    role = Column(String)
    original = Column(String)
    english = Column(String)
    parent_id = Column(Integer, ForeignKey('chat.id'))
    config = Column(JSON)

    parent = relationship("Chat", remote_side=[id], backref="children")