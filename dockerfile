# from python base image (python:version)
FROM python:3       

# tell docker that all commands are essentilly run from
WORKDIR /usr/src/app

# copy the local machine requirements into docker container
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# use COPY . . to copy everything in a current directory
COPY . .
# the space between .   . is to put a diff command between string
# its
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000","--reload"]

# build a docker image by running command
# > docker build -t fastapi .

# to check use
# > docker image ls