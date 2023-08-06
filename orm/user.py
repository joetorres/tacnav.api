from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime


class User(Base):
    __tablename__ = "app_user"

    id = Column(String, primary_key=True, index=True)
    dt_creation = Column(DateTime)  
    dt_update = Column(DateTime)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column (String)
    user_type = Column (String)

