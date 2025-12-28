# from fastapi import Depends, HTTPException, Path, APIRouter
# from typing import Annotated
# from pydantic import BaseModel, Field
# from sqlalchemy.orm import Session
#
# import models
# from database import SessionLocal
# from models import Todo
#
# router = APIRouter()
#
# # Dependency for DB session:
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# db_dependency = Annotated[Session, Depends(get_db)]
#
# class TodoRequest(BaseModel):
#     title: str = Field(min_length=3)
#     description: str = Field(min_length=3, max_length=100)
#     priority: int = Field(default=1, gt=0, lt=6)
#     complete: bool
#
#
# @router.get("/")
# async def read_all(db: db_dependency):
#     return db.query(models.Todo).all()
#
#
# # @app.get("/todo/todos/{todo_id}", status_code=status.HTTP_200_OK)
# # async def read_all(db: db_dependency, todo_id: int = Path(gt=0)):
# #     todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
# #     if todo_model is None:
# #         raise HTTPException(status_code=404, detail = "Todo Not Found")
# #     return todo_model
#
# @router.get("/todo/todos/{todo_id}")
# async def read_by_id(db: db_dependency, todo_id: int):
#     todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail = "Todo Not Found")
#     return todo_model
#
# # @app.post("/todo/", status_code=status.HTTP_201_CREATED)
# # def create(todo_request : TodoRequest, db: db_dependency):
# #     new_todo = Todos(**todo_request.model_dump())
# #     db.add(new_todo)
# #     db.commit()
# #     db.refresh(new_todo)
# #     return new_todo
#
# @router.post("/todo/")
# def create(todo_request : TodoRequest, db: db_dependency):
#     new_todo = Todo(**todo_request.model_dump())
#     db.add(new_todo)
#     db.commit()
#     db.refresh(new_todo)
#     return new_todo
#
# @router.put("/todo/{todo_id}") #status_code=status.HTTP_200_OK)
# # def update(todo_id: int = Path(gt=0) , todo_request : TodoRequest, db: db_dependency):   #L# non-default parameter follows default parameter
# def update(todo_request: TodoRequest, db: db_dependency, todo_id: int = Path(gt=0)):
#     todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail = "Todo Not Found")
#     todo_model.title = todo_request.title
#     todo_model.description = todo_request.description
#     todo_model.priority = todo_request.priority
#     todo_model.complete = todo_request.complete
#     db.add(todo_model)
#     db.commit()
#     db.refresh(todo_model)
#     return todo_model

from fastapi import Depends, HTTPException, Path, APIRouter
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
import models
from database import SessionLocal
from models import Todo
from .auth import get_current_user

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

# Dependency for DB session:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(default=1, gt=0, lt=6)
    complete: bool


@router.get("/")
async def read_all(db: db_dependency,user: user_dependency):
    # return db.query(models.Todo).all()
    return db.query(models.Todo).filter(Todo.owner_id == user.get('id')).all()


# @app.get("/todo/todos/{todo_id}", status_code=status.HTTP_200_OK)
# async def read_all(db: db_dependency, todo_id: int = Path(gt=0)):
#     todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail = "Todo Not Found")
#     return todo_model

@router.get("/{todo_id}")
async def read_by_id(db: db_dependency, todo_id: int, user: user_dependency):
    # todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    todo_model = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail = "Todo Not Found")
    return todo_model

# @app.post("/todo/", status_code=status.HTTP_201_CREATED)
# def create(todo_request : TodoRequest, db: db_dependency):
#     new_todo = Todos(**todo_request.model_dump())
#     db.add(new_todo)
#     db.commit()
#     db.refresh(new_todo)
#     return new_todo

@router.post("/")
def create(todo_request : TodoRequest, db: db_dependency,user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail = "Authentication Failed")
    # new_todo = Todo(**todo_request.model_dump())
    new_todo = Todo(**todo_request.model_dump(),owner_id = user.get('id'))
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.put("/{todo_id}") #status_code=status.HTTP_200_OK)
# def update(todo_id: int = Path(gt=0) , todo_request : TodoRequest, db: db_dependency):   #L# non-default parameter follows default parameter
def update(todo_request: TodoRequest, db: db_dependency,user : user_dependency, todo_id: int = Path(gt=0)):
    # todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    todo_model = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail = "Todo Not Found")
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model


@router.delete("/{todo_id}") #status_code=status.HTTP_200_OK)
# def delete(todo_request: TodoRequest, db: db_dependency,todo_id: int = Path(gt=0)):     #L# Request body is not required here as we are deleting
def delete(db: db_dependency,user : user_dependency,todo_id: int = Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.owner_id == user.get('id')).first()
    if todo_model is not None:
        db.query(Todo).filter(Todo.id == todo_id).delete()
        db.commit()
        return {"message": "Deleted successfully", "book": todo_model}
    raise HTTPException(status_code=404, detail="Todo Not Found")