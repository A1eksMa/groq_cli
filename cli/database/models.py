from sqlalchemy.orm import declarative_base

Base = declarative_base()

# We will define our database models here, for example:
#
# class Message(Base):
#     __tablename__ = 'messages'
#
#     id = Column(Integer, primary_key=True)
#     role = Column(String)
#     original = Column(String)
#     english = Column(String)
#     parent_id = Column(Integer, ForeignKey('messages.id'))
#
#     parent = relationship("Message", remote_side=[id], backref="children")
