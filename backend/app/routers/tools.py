from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db
from typing import List

router = APIRouter( tags=["tools"])


@router.get("/tools/all", response_model=list[schemas.ToolOut], response_model_by_alias=True)
def list_tools(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.tools.list(db, skip=skip, limit=limit)


@router.get("/tools/{tool_id}", response_model=schemas.ToolOut, response_model_by_alias=True)
def get_tool(tool_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.tools.get(db, tool_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Tool not found")
    return obj


@router.get("/tools/member/{memberId}", response_model=List[schemas.ToolOut], response_model_by_alias=True)
def get_tool_member(memberId: uuid.UUID, db: Session = Depends(get_db)):
    #obj = crud.tools.get(db, tool_id)
    obj = db.query(crud.tools.model).filter_by(memberId=memberId).all()
    return obj


@router.get("/tools/project/{projectId}", response_model=List[schemas.ToolOut], response_model_by_alias=True)
def get_tool_project(projectId: uuid.UUID, db: Session = Depends(get_db)):
    #obj = crud.tools.get(db, tool_id)
    obj = db.query(crud.tools.model).filter_by(projectId=projectId).all()
    return obj

@router.post("/tools/insert", response_model=schemas.ToolOut, status_code=status.HTTP_201_CREATED, response_model_by_alias=True
)
def create_tool(payload: schemas.ToolCreate, db: Session = Depends(get_db)):
    return crud.tools.create(db, payload)


@router.post("/tools/update", response_model=schemas.ToolOut, response_model_by_alias=True)
def update_tool(
     payload: schemas.ToolUpdate, db: Session = Depends(get_db)
):
    obj = crud.tools.get(db, payload.id)
    if not obj:
        raise HTTPException(status_code=404, detail="Tool not found")
    return crud.tools.update(db, obj, payload)


@router.delete("/tools/{tool_id}", response_model=schemas.ToolOut, response_model_by_alias=True)
def delete_tool(tool_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.tools.remove(db, tool_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Tool not found")
    return obj
