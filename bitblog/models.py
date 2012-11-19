from sqlalchemy import (
    func,
    Column,
    Boolean,
    DateTime,
    Integer,
    Text,
    String,
)
#from sqlalchemy.orm import relationship, backref
from bitblog.database import Base

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)

    created = Column(DateTime, default=func.now())

    slug = Column(String, unique=True)
    title = Column(String)
    content = Column(Text)

    is_published = Column(Boolean)