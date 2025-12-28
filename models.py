# from database import  Base
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
#
#
# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True,index=True)
#     email = Column(String,unique=True)
#     username = Column(String,unique=True)
#     firstname = Column(String)
#     lastname = Column(String)
#     hashed_password = Column(String)
#     is_active = Column(Boolean,default=True)
#     role = Column(String)
# #
# class Todo(Base):
#     __tablename__ = "todos"
#
#     id = Column(Integer, primary_key=True,index=True)
#     title= Column(String)
#     description = Column(String)
#     priority = Column(Integer)
#     complete = Column(Boolean,default=False)
#     owner_id = Column(Integer, ForeignKey("users.id"))

# from sqlalchemy import Column, Integer, String, Boolean
# from database import Base
#
# class Users(Base):
#     __tablename__ = "users"
# class Todos(Base):
#     __tablename__ = "todos"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String(200), unique=True, nullable=False)
#     username = Column(String(45), unique=True, nullable=False)
#     first_name = Column(String(45))
#     last_name = Column(String(45))
#     hashed_password = Column(String(200))
#     is_active = Column(Integer, default=1)
#     role = Column(String(45))
#
# from sqlalchemy import Column, Integer, String
# from database import Base
#
# class Todo(Base):
#     __tablename__ = "todos"
#
#     id = Column(Integer, primary_key=True, index=True)  # ✅ PRIMARY KEY
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     password = Column(String)

from database import  Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,index=True)
    email = Column(String,unique=True)
    username = Column(String,unique=True)
    firstname = Column(String)
    lastname = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)
    role = Column(String)

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True,index=True)
    title= Column(String)
    description = Column(String)
    priority = Column(String)
    complete = Column(Boolean,default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
