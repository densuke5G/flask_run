from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(16), unique=True, nullable=False)
    password = Column(String(512), nullable=False)
    posts = relationship('Post', back_populates='user')

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username!r}>'
    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    title = Column(String(256))
    body = Column(String(1000))
    created = Column(DateTime, default=datetime.datetime.now())
    user = relationship('User', back_populates='posts')

    def __init__(self, author_id=None, title=None, body=None, created=None):
        self.author_id = author_id
        self.title = title
        self.body = body
        self.created = created

    def __repr__(self):
        return f'<Post {self.title!r}>'
