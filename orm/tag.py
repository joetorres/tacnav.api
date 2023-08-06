from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Decimal

from orm.note import Note

class Tag(Base):
    __tablename__ = "tag"

    id = Column(String, primary_key=True, index=True)
    dt_creation = Column(DateTime)  
    dt_update = Column(DateTime)
    is_active = Column(Boolean, default=True)
    
    title = Column(String)
    description = Column(String)