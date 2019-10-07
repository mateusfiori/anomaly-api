# We will use Ubuntu for our image
FROM alpine:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apk add --no-cache python3 python3-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN apk --update add --no-cache gcc freetype-dev libpng-dev

RUN apk add --no-cache --virtual .build-deps \
    musl-dev \
    g++

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install --no-cache-dir fbprophet==0.5

# Install any needed packages specified in requirements.txt

RUN apk del .build-deps

EXPOSE 3333

CMD ["python3", "app.py"]