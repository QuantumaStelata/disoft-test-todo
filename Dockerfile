FROM python:3.10.6

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input
RUN python manage.py migrate --no-input
RUN python manage.py loaddata statuses
RUN python manage.py loaddata admin


