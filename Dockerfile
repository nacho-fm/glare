# Build based on latest ubuntu image for brevity's sake.
# In productizing, would likely fall back to a python3-alpine instance with explicit installation of dependencies
FROM ubuntu:latest

RUN apt update -y
RUN apt install -y python3-pip python3-dev build-essential

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Dependency management
COPY requirements.txt /usr/src/app/
COPY setup.py /usr/src/app/
COPY glare /usr/src/app/glare

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -e .
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose server port
EXPOSE 5000

# Run debug server (5000 port is baked into the server application logic. In prod, would move that out to config).
ENTRYPOINT ["python3"]
CMD ["-m", "glare.server"]
