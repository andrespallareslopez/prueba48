# Schema of Bases de datos IBIOLS

DataBase named: EFFICIENCY

Schema named: IBIOLS

Entities:
- Clients
- ProjectsClient
- Members
- MembersClient
- RagDatabases
- Tools

Details of entities, fields of every entities:

Fields of clients:
- _id : type of field guid, primary key.
- name: type of field  string 90 characters.
- description: type of field string 255 characters.

Fields of ProjectsClient:
- _id: type of field guid, primary key.
- clientId : id of entity client, type of field guid.
- name: type of field string 90 characters.
- description : type of field string 255 characters.
- ragId: 
- toolId: 

Fields of MembersClient:
- _id: type of field guid, primary key.
- clientId: id of entity client, type of field guid.
- name: type of field string 90 characters.
- email: type of field string 120 characters.
- role: type of field string 90 characters.
- status: type of field string 90 characters.

Fields of Members:
- _id: type of field guid, primary key.
- memberId: id of entity of MembersClient, type of field guid.
- projectId: id of entity of ProjectsClient, type of field guid.
- name: type of field string 90 characters.
- email: type of field string 120 characters.
- role: type of field string 90 characters.
- status: type of field string 90 characters.
- ragId: id of entity of RagDatabases, type of field guid
- toolId: id

Fields or RagDatabases:
- _id: type of field guid, primary key.
- memberId:  id of entity of MembersClient, type of field guid.
- projectId: id of entity of ProjectsClient, type of field guid.
- name: type of field string 90 characters.
- type: type of field string 90 characters.
- lastUpdate: type of field datetime

Fields of Tools:
- _id: type of field guid, primary key.
- memberId: id of entity of MembersClient, type of field guid.
- projectId: id of entity of ProjectsClient, type of field guid.
- name: type of field string 90 characters.
- type: type of field string 90 characters.
- permission: type of field string 90 characters.































