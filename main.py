# from fastapi import FastAPI, Depends, HTTPException, Path
# from pydantic import BaseModel, Field
# from sqlalchemy.orm import Session
# from starlette import status
# from typing import Annotated
#
# import models
# from models import Todo
# from database import engine, SessionLocal
# from routers import auth
#
# # Create tables
# models.Base.metadata.create_all(bind=engine)
#
# # FastAPI app
# app = FastAPI()
#
# # Include auth router
# app.include_router(auth.router)
#
# # Dependency for DB Session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# db_dependency = Annotated[Session, Depends(get_db)]
#
# # Pydantic Schema
# class TodoRequest(BaseModel):
#     title: str = Field(min_length=3)
#     description: str = Field(min_length=3, max_length=100)
#     priority: int = Field(default=1, gt=0, lt=6)
#     complete: bool
#
#     class Config:
#         orm_mode = True
#
#
# # READ ALL
# @app.get("/")
# async def read_all(db: db_dependency):
#     return db.query(Todo).all()
#
#
# # READ BY ID
# @app.get("/todo/{todo_id}")
# async def read_by_id(db: db_dependency, todo_id: int = Path(gt=0)):
#     todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail="Todo Not Found")
#     return todo_model
#
#
# # CREATE
# @app.post("/todo/", status_code=status.HTTP_201_CREATED)
# def create(todo_request: TodoRequest, db: db_dependency):
#     new_todo = Todo(**todo_request.dict())
#     db.add(new_todo)
#     db.commit()
#     db.refresh(new_todo)
#     return new_todo
#
#
# # UPDATE
# @app.put("/todo/{todo_id}")
# def update(todo_request: TodoRequest, db: db_dependency, todo_id: int = Path(gt=0)):
#     todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail="Todo Not Found")
#
#     todo_model.title = todo_request.title
#     todo_model.description = todo_request.description
#     todo_model.priority = todo_request.priority
#     todo_model.complete = todo_request.complete
#
#     db.commit()
#     return todo_model
#
#
# # DELETE
# @app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete(db: db_dependency, todo_id: int = Path(gt=0)):
#     todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail="Todo Not Found")
#
#     db.delete(todo_model)
#     db.commit()

from fastapi import FastAPI
import models
from database import engine
from routers import auth , todos , admin , users

app =FastAPI()

models.Base.metadata.create_all(bind=engine)# todos.db will be created automatically

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

