#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlmodel import SQLModel, Field


class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    text: str
    is_done: bool = Field(default=False)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "text": "Todo 1",
                "is_done": False
            }
        }
