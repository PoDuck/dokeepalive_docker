# first stage
FROM python:3.8.12 AS builder
COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

# second stage
FROM python:3.8.12-slim
WORKDIR /code

# copy dependencies and source files
COPY --from=builder /root/.local /root/.local
COPY ./src .
#RUN mkdir /conf

# update PATH
ENV PATH=/root/.local:$PATH

ENV PYTHONBUFFERED 1
CMD [ "python", "-u", "./dokeepalive.py" ]
