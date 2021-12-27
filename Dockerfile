# first stage
FROM python:3.8.12 AS builder
copy requirements.txt .

# install dependencies
RUN pip install --user -r requirements.txt

# second stage
FROM python:3.8.12-slim
WORKDIR /code

# copy dependencies and source files
COPY --from=builder /root/.local /root/.local
COPY ./src .

# update PATH
ENV PATH=/root/.local:$PATH

ENV PYTHONBUFFERED 1
CMD [ "python", "-u", "./dokeepalive.py" ]

# RUN apt-get update
# RUN apt-get -y upgrade
# RUN apt-get install -y python3-digitalocean
# RUN mkdir /usr/src/app
# WORKDIR /usr/src/app
# COPY ./requirements.txt .
# ENV PYTHONBUFFERED 1
# COPY . .
