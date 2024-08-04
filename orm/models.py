from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..flaskr.db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(16), unique=True, nullable=False)
    password = Column(String(16), nullable=False)
    post = relationship(back_populates='users')

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username!r}>'
    
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(256))
    body = Column(String(1000))
    created = Column(DateTime)

    def __init__(self, author_id=None, title=None, body=None, created=None):
        self.author_id = author_id
        self.title = title
        self.body = body
        self.created = created

    def __repr__(self):
        return f'<Post {self.title!r}>'
