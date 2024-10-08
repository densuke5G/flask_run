from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
from flaskr.models import User, Post

password = config.DATABASE_PASSWORD
engine = create_engine('mysql+pymysql://root:' + password + '@localhost:3306/flask_run?charset=utf8')
Session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = Session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    
    Base.metadata.create_all(bind=engine)

def regist_user(username, password):
    """Register a new user in the database."""
    try:
        db_session = Session()
        new_user = User(username=username, password=password)
        db_session.add(new_user)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        print(f"Error while adding user: {e}")
    finally:
        db_session.close()

def select_user_by_username(username):
    """Retrieve a user by username."""
    try:
        db_session = Session()
        user = db_session.query(User).filter(User.username == username).first()
        return user
    except Exception as e:
        print(f"Error while retrieving user: {e}")
    finally:
        db_session.close()

def select_user_by_user_id(user_id):
    """Retrieve a user by user_id."""
    try:
        db_session = Session()
        user = db_session.query(User).filter(User.id == user_id).first()
        return user
    except Exception as e:
        print(f"Error while retrieving user: {e}")
    finally:
        db_session.close()

def select_posts():
    """Retrieve a posts and join user table."""
    try:
        db_session = Session()
        posts = db_session.query(Post).join(User, User.id == Post.author_id).all()
        return posts
    except Exception as e:
        print(f"Error while retrieving posts: {e}")
    finally:
        db_session.close()

def create_post(title, body, author_id):
    """create a new post"""
    try:
        db_session = Session()
        new_post = Post(title=title, body=body, author_id=author_id)
        db_session.add(new_post)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        print(f"Error while adding user: {e}")
    finally:
        db_session.close()

def select_post_by_post_id(id):
    """Retrieve a post by post_id."""
    try:
        db_session = Session()
        post = db_session.query(Post).filter(Post.id == id).first()
        return post
    except Exception as e:
        print(f"Error while retrieving post: {e}")
    finally:
        db_session.close()

def update_post(title, body, id):
    """update a post"""
    try:
        db_session = Session()
        post = db_session.query(Post).filter(Post.id == id).first()
        post.title = title
        post.body = body
        db_session.commit()
    except Exception as e:
        print(f"Error while updating post: {e}")
    finally:
        db_session.close()

def delete_post(id):
    """delete a post"""
    try:
        db_session = Session()
        post = db_session.query(Post).filter(Post.id == id).first()
        db_session.delete(post)
        db_session.commit()
    except Exception as e:
        print(f"Error while deleting post: {e}")
    finally:
        db_session.close()
