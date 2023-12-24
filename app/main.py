#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

from .db.connection import conn
from .routes.bootstrap import bs_router
from .routes.events import event_router
from .routes.main import main_router
from .routes.users import user_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# regist routes
app.include_router(user_router, prefix="/users", tags=["User"])
app.include_router(main_router, prefix="/main", tags=["Main"])
app.include_router(event_router, prefix="/events", tags=["Event"])
app.include_router(bs_router, prefix="/bs", tags=["Bootstrap"])


@app.on_event("startup")
def on_startup():
    conn()


@app.get("/")
async def home():
    return RedirectResponse(url="/users/signin/")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
