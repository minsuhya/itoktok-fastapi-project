#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter, Request, HTTPException, status

from ..models.users import User, UserSignIn
from ..main import templates

bs_router = APIRouter(tags=["Bootstrap"])


@bs_router.get("/")
def bs_main(request: Request):
    return templates.TemplateResponse('main.html',
                                      context={'request': request})
