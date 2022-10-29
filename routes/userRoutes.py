from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.user import users
from schemas.user import User

userRoutes = APIRouter()

# Obtener todos los usuarios
@userRoutes.get("/users")
def getAllUsers():
    return conn.execute(users.select()).fetchall()

# Obtener un usuario a partir de un Id
@userRoutes.get("/users/{id}")
def getUserById(id: int):
    return conn.execute(users.select().where(users.c.id == id)).first()

# Eliminar un usuario
@userRoutes.delete("/users/{id}")
def deleteUser(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

# Crear un usuario
@userRoutes.post("/users")
def storeUser(user : User):
    newUser = {"id": user.id, "name": user.name, "email": user.email, "password": user.password}
    conn.execute(users.insert().values(user))
    return conn.execute(users.select().where(users.c.id == user.id)).first()

# Editar un usuario
@userRoutes.put("/users/{id}")
def updateUser(id: int, user: User):
    conn.execute(users.update().values(name = user.name, email = user.email, password = user.password)
    .where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()
