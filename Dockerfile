FROM python:3.6.9-slim-stretch

RUN apt-get -y update  && apt-get install -y \
    python3-dev \
    libpng-dev \
    apt-utils \
    build-essential \
    python-psycopg2 \
    python-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools
RUN pip install cython
RUN pip install numpy
RUN pip install matplotlib
RUN pip install pystan
RUN pip install psycopg2-binary
RUN pip install motor
RUN pip install tornado
RUN pip install luminol
RUN pip install py-healthcheck==1.9.0
RUN pip install --upgrade plotly
RUN pip install fbprophet
RUN pip install sqlalchemy

WORKDIR /forecast
COPY . /forecast/

EXPOSE 7777

ENTRYPOINT [ "python", "app.py" ]