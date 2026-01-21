from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db

router = APIRouter(prefix="/tools", tags=["tools"])


@router.get("/", response_model=list[schemas.ToolOut])
def list_tools(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.tools.list(db, skip=skip, limit=limit)


@router.get("/{tool_id}", response_model=schemas.ToolOut)
def get_tool(tool_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.tools.get(db, tool_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Tool not found")
    return obj


@router.post("/", response_model=schemas.ToolOut, status_code=status.HTTP_201_CREATED)
def create_tool(payload: schemas.ToolCreate, db: Session = Depends(get_db)):
    return crud.tools.create(db, payload)


@router.put("/{tool_id}", response_model=schemas.ToolOut)
def update_tool(
    tool_id: uuid.UUID, payload: schemas.ToolUpdate, db: Session = Depends(get_db)
):
    obj = crud.tools.get(db, tool_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Tool not found")
    return crud.tools.update(db, obj, payload)


@router.delete("/{tool_id}", response_model=schemas.ToolOut)
def delete_tool(tool_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.tools.remove(db, tool_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Tool not found")
    return obj
