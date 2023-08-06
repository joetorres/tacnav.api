#!/usr/bin/python3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import log
#from routes import midia, user, login, project, auth
from orm.database import createAll

createAll()

app = FastAPI(title="TacNav API", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.include_router(login.router)

@app.get("/")
async def itsAlive():
    return {"message": "It's Alive!"}

