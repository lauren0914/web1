FROM python:3.9.0

# home 이라는 경로에서 명령어 실행할 거다
WORKDIR /home/

RUN echo 'lksmaoidmf'

RUN git clone https://github.com/lauren0914/web1.git

# 위에 있는 web1이랑 똑같아야됨. 그러니까 파이참 프로젝트명이랑은 관계없이 깃허브 저장소명이랑 똑같은 걸로
WORKDIR /home/web1/

RUN echo "SECRET_KEY=django-insecure-y+)qw*n6-^i8^bq02f-+ns=0-9$x3md@m=4p*tt#_37fpb0x16" > .env

# 로컬에서 설치한 라이브러리를 가상환경에서도 설치하라
RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

# 여기에는 소스코드만 있는 거라 migrate 작업 통해서 DB생성해야됨

EXPOSE 8000

# "" 로 넣어야됨 '' 작동 안 함
CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=web_1.settings.deploy && python manage.py migrate --settings=web_1.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=web_1.settings.deploy web_1.wsgi --bind 0.0.0.0:8000"]
