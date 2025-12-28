# 1from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread': False})
#
# SessionLocal= sessionmaker(autocommit=False,autoflush=False, bind=engine)
# Base = declarative_base()
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
#
# DATABASE_URL = "sqlite:///./todos.db"
# # DATABASE_URL = "mysql+pymysql://root:Gowtham2004@%40/@127.0.0.1:3306/todoapp"
#
# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False}  # Only for SQLite
# )
#
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )
#
# Base = declarative_base()
#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///todoapp.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
#
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Gowtham2004%40@127.0.0.1:3306/todoapp"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



