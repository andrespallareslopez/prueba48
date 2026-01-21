from __future__ import annotations

from sqlalchemy.orm import Session

from . import models, schemas


class CRUDBase:
    def __init__(self, model):
        self.model = model

    def get(self, db: Session, item_id):
        return db.get(self.model, item_id)

    def list(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in):
        db_obj = self.model(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj, obj_in):
        data = obj_in.model_dump(exclude_unset=True)
        for field, value in data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, item_id):
        db_obj = db.get(self.model, item_id)
        if not db_obj:
            return None
        db.delete(db_obj)
        db.commit()
        return db_obj


clients = CRUDBase(models.Clients)
projects = CRUDBase(models.ProjectsClient)
members_client = CRUDBase(models.MembersClient)
rag_databases = CRUDBase(models.RagDatabases)
tools = CRUDBase(models.Tools)
members = CRUDBase(models.Members)
