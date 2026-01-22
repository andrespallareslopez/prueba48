
--Crear la base de datos

--CREATE DATABASE EFFICIENCY


-- Schema for EFFICIENCY API
-- Generated from SQLAlchemy models in backend/app/models.py

-- Enable UUID generation
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Schema
CREATE SCHEMA IF NOT EXISTS ibiols;

-- Tables
CREATE TABLE IF NOT EXISTS ibiols.clients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(90) NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS ibiols.projects_client (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES ibiols.clients(id) ON DELETE CASCADE,
    name VARCHAR(90) NOT NULL,
    description VARCHAR(255),
    rag_id UUID,
    tool_id UUID
);

CREATE TABLE IF NOT EXISTS ibiols.members_client (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES ibiols.clients(id) ON DELETE CASCADE,
    name VARCHAR(90) NOT NULL,
    email VARCHAR(120) NOT NULL,
    role VARCHAR(90),
    status VARCHAR(90)
);

CREATE TABLE IF NOT EXISTS ibiols.rag_databases (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    member_id UUID NOT NULL REFERENCES ibiols.members_client(id) ON DELETE CASCADE,
    project_id UUID NOT NULL REFERENCES ibiols.projects_client(id) ON DELETE CASCADE,
    name VARCHAR(90) NOT NULL,
    type VARCHAR(90),
    last_update TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ibiols.tools (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    member_id UUID NOT NULL REFERENCES ibiols.members_client(id) ON DELETE CASCADE,
    project_id UUID NOT NULL REFERENCES ibiols.projects_client(id) ON DELETE CASCADE,
    name VARCHAR(90) NOT NULL,
    type VARCHAR(90),
    permission VARCHAR(90)
);

CREATE TABLE IF NOT EXISTS ibiols.members (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    member_id UUID NOT NULL REFERENCES ibiols.members_client(id) ON DELETE CASCADE,
    project_id UUID NOT NULL REFERENCES ibiols.projects_client(id) ON DELETE CASCADE,
    name VARCHAR(90) NOT NULL,
    email VARCHAR(120) NOT NULL,
    role VARCHAR(90),
    status VARCHAR(90),
    rag_id UUID REFERENCES ibiols.rag_databases(id) ON DELETE SET NULL,
    tool_id UUID REFERENCES ibiols.tools(id) ON DELETE SET NULL
);
