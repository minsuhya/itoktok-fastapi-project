#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import make_dataclass

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from sqlmodel import select

from ..db.connection import get_session
from ..main import templates
from ..models.centers import CenterInfo
from ..models.users import User, UserSignIn

user_router = APIRouter(tags=["User"])


@user_router.get("/signup")
def sign_up_form(request: Request):
    return templates.TemplateResponse('users/sign_up_form.html',
                                      context={'request': request})


@user_router.post("/signup")
async def sign_up_user(request: Request,
                       user_id: str = Form(...),
                       password: str = Form(...),
                       hp: str = Form(...),
                       email: str = Form(...),
                       center_name: str = Form(...),
                       user_name: str = Form(...),
                       biz_no: str = Form(...),
                       memo: str = Form(...),
                       session=Depends(get_session)):
    # 폼  데이터 검증
    form_data = await request.form()
    form = make_dataclass("Form", form_data.keys())(**form_data)
    user = session.exec(
        select(User).where(User.user_id == form.user_id)).first()

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="사용자가 이미 존재합니다.")

    # 센터 정보 생성
    new_center = CenterInfo(center_name=form.center_name,
                            center_ceo=form.user_name,
                            center_tel=form.hp,
                            center_zipcode="",
                            center_addr="",
                            center_addr2="")
    session.add(new_center)
    session.commit()
    session.refresh(new_center)

    # 사용자 정보 생성
    new_user = User(user_id=form.user_id,
                    password=form.password,
                    user_level=1,
                    hp=form.hp,
                    email=form.email,
                    center_id=new_center.id,
                    user_name=form.user_name,
                    biz_no=form.biz_no,
                    memo=form.memo)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    #  return event
    return {"message": "사용자가 생성되었습니다.", "user": new_user}


@user_router.get("/signin")
def sign_in_form(request: Request):
    return templates.TemplateResponse('users/sign_in_form.html',
                                      context={'request': request})


@user_router.post("/signin")
async def sign_in_user(user: UserSignIn) -> dict:
    users = {}
    if user.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    if users[user.email].password != user.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Wrong password")
    #  return users[user.email]
    return {"message": "User signed in"}


@user_router.get("/forgot-password")
def forgot_password_form(request: Request):
    return templates.TemplateResponse('users/forgot-password.html',
                                      context={'request': request})


@user_router.post("/forgot-password")
def forgot_password(request: Request):
    return {"message": "User signed in", "request": request}


@user_router.get("/list")
def user_list(request: Request, session=Depends(get_session)):
    users = session.exec(select(User)).all()
    return templates.TemplateResponse('users/list.html',
                                      context={
                                          'request': request,
                                          'users': users
                                      })


@user_router.get("/calendar2")
def calendar2(request: Request):
    return templates.TemplateResponse('calendar2.html',
                                      context={'request': request})
