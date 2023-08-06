from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Decimal

from orm.note import Note

class File(Base):
    __tablename__ = "file"

    id = Column(String, primary_key=True, index=True)
    dt_creation = Column(DateTime)  
    dt_update = Column(DateTime)
    is_active = Column(Boolean, default=True)
    
    path = Column(String)
    original_name = Column(String)
    mime_type = Column(String)
    note_id = Column(String, ForeignKey=Note.id)
    

    