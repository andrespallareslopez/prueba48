from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


def to_camel(value: str) -> str:
    parts = value.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


class APIBase(BaseModel):
    model_config = ConfigDict(
        
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )

class ClientInsert(BaseModel):
    name: str
    description: str | None = None

class ClientBase(APIBase):
    name: str
    description: str | None = None


class ClientCreate(ClientBase):
    pass


class ClientUpdate(APIBase):
    id: uuid.UUID 
    name: str | None = None
    description: str | None = None


class ClientOut(ClientBase):
    id: uuid.UUID


class ProjectBase(APIBase):
    clientId: uuid.UUID
    name: str
    description: str | None = None
    


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(APIBase):
    id: uuid.UUID
    clientId: uuid.UUID | None = None
    name: str | None = None
    description: str | None = None
   


class ProjectOut(ProjectBase):
    id: uuid.UUID


class MemberClientBase(APIBase):
    clientId: uuid.UUID
    name: str
    email: EmailStr
    role: str | None = None
    status: str | None = None


class MemberClientCreate(MemberClientBase):
    pass


class MemberClientUpdate(APIBase):
    id: uuid.UUID
    clientId: uuid.UUID | None = None
    name: str | None = None
    email: EmailStr | None = None
    role: str | None = None
    status: str | None = None


class MemberClientOut(MemberClientBase):
    id: uuid.UUID


class RagDatabaseBase(APIBase):
    memberId: uuid.UUID | None = None
    projectId: uuid.UUID | None = None
    name: str
    type: str | None = None
    lastUpdate: datetime | None = None


class RagDatabaseCreate(RagDatabaseBase):
    pass


class RagDatabaseUpdate(APIBase):
    id: uuid.UUID
    memberId: uuid.UUID | None = None
    projectId: uuid.UUID | None = None
    name: str | None = None
    type: str | None = None
    lastUpdate: datetime | None = None


class RagDatabaseOut(RagDatabaseBase):
    id: uuid.UUID


class ToolBase(APIBase):
    memberId: uuid.UUID | None = None
    projectId: uuid.UUID | None = None
    name: str
    type: str | None = None
    permission: str | None = None


class ToolCreate(ToolBase):
    pass


class ToolUpdate(APIBase):
    id: uuid.UUID
    memberId: uuid.UUID | None = None
    projectId: uuid.UUID | None = None
    name: str | None = None
    type: str | None = None
    permission: str | None = None


class ToolOut(ToolBase):
    id: uuid.UUID


class MemberBase(APIBase):
    memberId: uuid.UUID
    projectId: uuid.UUID
    name: str
    email: EmailStr
    role: str | None = None
    status: str | None = None
   


class MemberCreate(MemberBase):
    pass


class MemberUpdate(APIBase):
    id: uuid.UUID
    memberId: uuid.UUID | None = None
    projectId: uuid.UUID | None = None
    name: str | None = None
    email: EmailStr | None = None
    role: str | None = None
    status: str | None = None
  


class MemberOut(MemberBase):
    id: uuid.UUID
