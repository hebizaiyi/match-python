from typing import Union
from fastapi import FastAPI
from apis.sys_user import router as sys_user_router
app = FastAPI()

@app.get("/")

def read_root(): 
    return { "hello": "world"}

app.include_router(sys_user_router)