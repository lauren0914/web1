from .base import *
# base 파일에서 생성했던 모든 것을 가져오기

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
DEBUG = False

# * : 모든 host가 들어올 수 있다
ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
