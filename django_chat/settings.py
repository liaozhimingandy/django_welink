# -*- coding: utf-8 -*-

"""
Django settings for django_chat project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

from django import get_version

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "APP_SECRET_KEY", "django-insecure-&(s=fs#s3b9&=8&y_+bhzquk_1-uq)iu@=v=%+&qegp9958%e$"
)

# 应用版本号
VERSION = (23, 0, 2, "alpha", 18)
__version__ = get_version(VERSION)
APP_NAME = "chat"
# id前缀
PREFIX_ID = os.getenv("PREFIX_ID", "cid_")

with open(os.path.join(BASE_DIR, 'AppVersionHash.txt')) as fp:
    APP_COMMIT_HASH = fp.readline()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv("APP_DEBUG", 1))
ALLOWED_HOSTS = os.getenv("APP_DJANGO_ALLOWED_HOSTS", "*").split(",")
CSRF_TRUSTED_ORIGINS = os.getenv("APP_CSRF_TRUSTED_ORIGINS", "http://*,https://*").split(",")

# Application definition
# 官方app
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",  # 站点使用
    "django.contrib.admindocs"
]
# 第三方app
THIRD_PARTY_APPS = [
    'corsheaders',  # 添加：跨域组件
]

# 本地app
LOCAL_APPS = [
    "account",
    "post",
    "comment",
    "like",
    "oauth"
    # Your stuff: custom apps go here
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_chat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_chat.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("APP_DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.getenv("APP_DB_NAME", "chat"),
        "USER": os.getenv("APP_DB_USER", "zhiming"),
        "PASSWORD": os.getenv("APP_DB_PASSWORD", "zhiming"),
        "HOST": os.getenv("APP_DB_HOST", "db.chat.alsoapp.com"),
        "PORT": os.getenv("APP_DB_PORT", "5432"),
        'OPTIONS': {
            'options': '-c timezone=Asia/Shanghai',
        },
    },
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'chat.db',
    },
    'default1': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'chat.db',
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = os.getenv('APP_LANGUAGE_CODE', 'zh-hans')

TIME_ZONE = os.getenv('APP_TIME_ZONE', 'Asia/Shanghai')  # 设置为中国上海时区，即北京时间

USE_I18N = True

USE_TZ = True  # 启用时区支持

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# 静态文件
STATIC_URL = os.getenv("APP_STATIC_URL", 'static/')
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# 多媒体文件
MEDIA_URL = os.getenv("APP_MEDIA_URL", 'media/')
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
# python manage.py collectstatic 收集文件到下面文件文件夹里
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 默认为False，设置True许跨域时携带Cookie
# 用于处理跨域问题
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    'http://localhost:8080',
    'https://alsoapp.gnway.cc',
    'http://alsoapp.gnway.cc',
    'http://welink.alsoapp.com',
    'https://welink.alsoapp.com',
    # 这里需要注意： 1. 必须添加http://否则报错（https未测试） 2. 此地址就是允许跨域的地址，即前端地址
)

##########################################################################################
# 站点
SITE_ID = os.getenv('APP_SITE_ID', 2024)

##########################################################################################
# MinIO服务器地址及认证信息
MINIO_ACCESS_KEY = os.getenv('APP_MINIO_ACCESS_KEY', 'chat')
MINIO_SECRET_KEY = os.getenv('APP_MINIO_SECRET_KEY', 'chat1234')
MINIO_SCHEMA = os.getenv('APP_MINIO_SCHEMA', 'http://')
MINIO_ENDPOINT = os.getenv('APP_MINIO_ENDPOINT', '172.16.33.188:10005')  # MinIO服务器地址
MINIO_BUCKET = os.getenv('APP_MINIO_BUCKET', 'chat')

# 设置文件默认存储
DEFAULT_FILE_STORAGE = 'post.MyStorage.MinioStorage'
##########################################################################################

##########################################################################################
# django-ninja配置
NINJA_PAGINATION_PER_PAGE = 10  # 默认页面大小
NINJA_PAGINATION_MAX_LIMIT = 10  # 每页的最大结果数
##########################################################################################

