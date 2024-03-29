import uuid

from django.db import models
from django.core.management.utils import get_random_string


def salt_default():
    return str(uuid.uuid4()).replace('-', '')[:8]


def app_secret_default():
    return get_random_string(32)


# Create your models here.
class App(models.Model):
    app_id = models.UUIDField(default=uuid.uuid4, db_comment="appid")
    app_secret = models.CharField(default=app_secret_default, max_length=128, db_comment="应用密钥",
                                  help_text="应用密钥")
    salt = models.CharField(default=salt_default, max_length=8, db_comment="盐", help_text="盐")
    app_name = models.CharField("应用名称", max_length=64, db_comment="应用名称", help_text="应用名称")
    app_en_name = models.CharField("应用英文名称", max_length=64, db_comment="应用英文名称", help_text="应用英文名称",
                                   null=True, blank=True)
    is_active = models.BooleanField("激活状态", default=True, db_comment="激活状态", help_text="激活状态")
    gmt_created = models.DateTimeField("创建日期时间", auto_now_add=True, help_text="创建日期时间",
                                       db_comment="创建日期时间")
    gmt_updated = models.DateTimeField("最后更新日期时间", auto_now=True, help_text="最后更新日期时间",
                                       db_comment="最后更新日期时间")

    class Meta:
        verbose_name = "应用信息"
        verbose_name_plural = verbose_name
