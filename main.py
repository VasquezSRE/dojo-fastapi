from fastapi import FastAPI
from routes.userRoutes import userRoutes

app = FastAPI()

app.include_router(userRoutes)









