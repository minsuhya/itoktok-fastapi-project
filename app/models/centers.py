#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class CenterInfo(SQLModel, table=True):
    """Center."""

    id: Optional[int] = Field(default=None, primary_key=True)
    center_name: str = Field(default=None)
    center_ceo: str = Field(default=None)
    center_tel: str = Field(default=None)
    center_zipcode: str = Field(default=None)
    center_addr: str = Field(default=None)
    center_addr: str = Field(default=None)
    # 승인 여부
    is_approved: bool = Field(default=False)
    # datetime field
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    deleted_at: Optional[datetime] = Field(default=None)

    class Config:
        """Config."""
        json_schema_extra = {
            "example": {
                "center_name": "아이톡톡센터",
                "center_ceo": "홍길동"
            }
        }


class CenterInfoUpdate(SQLModel):
    """CenterUpdate."""

    center_name: str
    center_ceo: str

    class Config:
        """Config."""

        json_schema_extra = {
            "example": {
                "center_name": "아이톡톡센터",
                "center_ceo": "홍길동"
            }
        }
