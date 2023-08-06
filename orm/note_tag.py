from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Decimal

from orm.note import Note
from orm.tag import Tag

class Point(Base):
    __tablename__ = "point"
    id = Column(String, primary_key=True, index=True)
    tag_id = Column(String, ForeignKey=Tag.id)
    note_id = Column(String, ForeignKey=Note.id)

    