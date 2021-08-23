"""
Django settings for web_1 project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.conf.global_settings import STATIC_ROOT
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent
# resolve 까지 settings.py 파일의 경로를 나타냄. 거기에 부모의 경로를 넣고 있음. 부모경로가 web_1 근데 부모가 또 있음. 프로젝트 폴더
# 즉, 최상위 프로젝트폴더의 .env를 읽어서
env_list = dict()
local_env = open(os.path.join(BASE_DIR, '.env'))
# os : 운영체제 경로에 관련된 모듈이 들어가있는 게 os.path 임/ join : 합친다. base_dir + env

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')
    # 줄이 여러개 넣는다고 하면 줄바꿈줄이 항상 포함될 것이기 때문에 그건 실제 밸류가 아니기 때문에 없애줌
    start = line.find('=')
    # 처음 만난 값의 인덱스를 돌려줌. = 를 기준으로 슬라이싱하기 위해서.
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# * : 모든 host가 들어올 수 있다
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'accountapp',
    'profileapp',
    'articleapp',
    'commentapp',
    'projectapp',
    'subscribeapp',
    'likeapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web_1.urls'

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

WSGI_APPLICATION = 'web_1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# BASE_DIR: 최상위 프로젝트
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# 이미지 업로드 받기 위해서 지정해주는 거
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = reverse_lazy('accountapp:hello_world')
LOGOUT_REDIRECT_URL = reverse_lazy('accountapp:login')