
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
    _id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(90) NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS ibiols.projects_client (
    _id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clientId UUID NOT NULL REFERENCES ibiols.clients(_id) ON DELETE CASCADE,
    name VARCHAR(90) NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS ibiols.members_client (
    _id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clientId UUID NOT NULL REFERENCES ibiols.clients(_id) ON DELETE CASCADE,
    name VARCHAR(90) NOT NULL,
    email VARCHAR(120) NOT NULL,
    role VARCHAR(90),
    status VARCHAR(90)
);


CREATE TABLE IF NOT EXISTS ibiols.members (
    _id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    memberId UUID NOT NULL REFERENCES ibiols.members_client(_id) ON DELETE CASCADE,
    projectId UUID NOT NULL REFERENCES ibiols.projects_client(_id) ON DELETE CASCADE,
    name VARCHAR(90) NOT NULL,
    email VARCHAR(120) NOT NULL,
    role VARCHAR(90),
    status VARCHAR(90)
   
);


CREATE TABLE IF NOT EXISTS ibiols.rag_databases (
    _id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    memberId UUID  REFERENCES ibiols.members(_id) ON DELETE CASCADE,
    projectId UUID  REFERENCES ibiols.projects_client(_id) ON DELETE CASCADE,
    name VARCHAR(90) NOT NULL,
    type VARCHAR(90),
    last_update TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ibiols.tools (
    _id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    memberId UUID  REFERENCES ibiols.members(_id) ON DELETE CASCADE,
    projectId UUID  REFERENCES ibiols.projects_client(_id) ON DELETE CASCADE,
    name VARCHAR(90) NOT NULL,
    type VARCHAR(90),
    permission VARCHAR(90)
);