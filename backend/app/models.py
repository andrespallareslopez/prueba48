from __future__ import annotations

import uuid

from sqlalchemy import MetaData, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    metadata = MetaData(schema="ibiols")


class Clients(Base):
    __tablename__ = "clients"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))


class ProjectsClient(Base):
    __tablename__ = "projects_client"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ibiols.clients.id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))
    rag_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    tool_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))


class MembersClient(Base):
    __tablename__ = "members_client"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ibiols.clients.id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[str | None] = mapped_column(String(90))
    status: Mapped[str | None] = mapped_column(String(90))


class RagDatabases(Base):
    __tablename__ = "rag_databases"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    member_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ibiols.members_client.id", ondelete="CASCADE"),
        nullable=False,
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ibiols.projects_client.id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    type: Mapped[str | None] = mapped_column(String(90))
    last_update: Mapped[DateTime | None] = mapped_column(DateTime)


class Tools(Base):
    __tablename__ = "tools"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    member_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ibiols.members_client.id", ondelete="CASCADE"),
        nullable=False,
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ibiols.projects_client.id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    type: Mapped[str | None] = mapped_column(String(90))
    permission: Mapped[str | None] = mapped_column(String(90))


class Members(Base):
    __tablename__ = "members"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    member_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ibiols.members_client.id", ondelete="CASCADE"),
        nullable=False,
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ibiols.projects_client.id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[str | None] = mapped_column(String(90))
    status: Mapped[str | None] = mapped_column(String(90))
    rag_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ibiols.rag_databases.id", ondelete="SET NULL"),
    )
    tool_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ibiols.tools.id", ondelete="SET NULL"),
    )
