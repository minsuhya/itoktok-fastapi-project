#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import Optional
from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    """User."""

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(default=None, unique=True)
    password: str = Field(default=None)
    user_level: int = Field(default=1)  # 1: admin, 2: teacher, 3: student
    user_name: str = Field(default=None)
    hp: str = Field(default=None)
    email: EmailStr = Field(default=None)
    center_id: str = Field(default=None)
    biz_no: str = Field(default=None)
    memo: str = Field(default=None)
    # datetime field
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    deleted_at: Optional[datetime] = Field(default=None)

    class Config:
        """Config."""
        json_schema_extra = {
            "example": {
                "user_id": "fastapi",
                "password": "123456",
                "user_level": 1,
                "hp": "010-1234-5678",
                "email": "user@mail.com",
                "center_name": "아이톡톡센터",
                "biz_no": "123-45-67890",
                "memo": "메모"
            }
        }


class UserSignIn(SQLModel):
    """UserSignIn."""

    user_id: str
    password: str

    class Config:
        """Config."""

        json_schema_extra = {
            "example": {
                "user_id": "fastapi",
                "password": "123456"
            }
        }
