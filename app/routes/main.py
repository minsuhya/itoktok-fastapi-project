#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter, Request, HTTPException, status

from ..models.users import User, UserSignIn
from ..main import templates

main_router = APIRouter(tags=["Main"])


@main_router.get("/")
def main(request: Request):
    return templates.TemplateResponse('main/main.html',
                                      context={'request': request})
