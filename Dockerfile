FROM python:3.9-alpine3.13 
LABEL maintainer="mustfaozcan"

ENV PYTHONUNBUFFERED 1 

COPY ./requirements.txt /tmp/requirements.txt 
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

COPY ./app /app
WORKDIR /app
EXPOSE 8000

# Sanal ortam oluşturuluyor
ARG DEV=false
RUN python -m venv /py && \   
    # Pip güncelleniyor             
    /py/bin/pip install --upgrade pip && \
    # Bağımlılıklar yükleniyor  
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt; fi && \
    rm -rf /tmp && \
    # Kullanıcı ekleniyor
    adduser \ 
        --disabled-password \
        --no-create-home \
        django-user

# Sanal ortam PATH'e ekleniyor        
ENV PATH="/py/bin:$PATH"

USER django-user


