FROM python:3.8-alpine3.10

ENV USR_LOCAL_BIN=/usr/local/bin  \
    PROJECT_ROOT=/application

ENV PYTHONPATH=$PYTHONPATH:$PROJECT_ROOT

ENV RUNTIME_PACKAGES \
    libev \
    pcre \
    postgresql-dev \
    libxslt-dev \
    libmagic \
    libjpeg

ENV BUILD_PACKAGES \
    libev-dev \
    git \
    build-base \
    pcre-dev \
    gcc \
    linux-headers \
    libc-dev \
    musl-dev \
    jpeg-dev \
    zlib-dev \
    libxml2-dev


COPY ./Pipfile ./Pipfile.lock $PROJECT_ROOT/
WORKDIR $PROJECT_ROOT

RUN pip install --upgrade wheel pipenv \
    && apk --no-cache add --virtual build-deps $BUILD_PACKAGES \
    && apk --no-cache add $RUNTIME_PACKAGES \
    && set -ex && pipenv install --deploy --system --dev \
    && apk del build-deps

COPY . $PROJECT_ROOT/

COPY ./compose/app/start_gunicorn $USR_LOCAL_BIN/

RUN chmod +x $USR_LOCAL_BIN/start_gunicorn

CMD start_gunicorn
