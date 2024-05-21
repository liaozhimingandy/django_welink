#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: settings.py
    @File： api.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-04-18 15:35
    @Desc: 
================================================="""

from ninja import Router, Schema

from like.models import Like

router = Router(tags=["like"])


class LikeSchema(Schema):
    account_id: str


@router.get("/{app_id}/{post_id}/{account_id}/")
def get_likes(request, app_id: str, post_id: str, account_id: str):
    """
    获取点赞数
    :param request:
    :param app_id: 应用ID
    :param post_id: 帖子ID
    :param account_id: 当前用户
    :return:
    """
    count_like = Like.objects.filter(app_id=app_id, post_id=post_id).count()
    is_like = Like.objects.filter(app_id=app_id, post_id=post_id, account_id=account_id).exists()
    return {"count": count_like, "is_like": is_like}


@router.delete("/{app_id}/{post_id}/{account_id}/")
def delete_like(request, app_id: str, post_id: str, account_id: str):
    """
    取消点赞
    :param account_id:
    :param request:
    :param app_id:
    :param post_id:
    :return:
    """
    Like.objects.filter(app_id=app_id, post_id=post_id, account_id=account_id).delete()
    count_like = Like.objects.filter(app_id=app_id, post_id=post_id).count()

    return {"count": count_like, "is_like": False}


@router.post("/{app_id}/{post_id}/")
def create_like(request, app_id: str, post_id: str, payload: LikeSchema):
    """
    点赞
    :param request:
    :param app_id:
    :param post_id:
    :param payload:
    :return:
    """
    payload_dict = payload.dict()

    Like(app_id=app_id, post_id=post_id, account_id=payload_dict["account_id"]).save()
    count_like = Like.objects.filter(app_id=app_id, post_id=post_id).count()

    return {"count": count_like, "is_like": True}


if __name__ == "__main__":
    pass
