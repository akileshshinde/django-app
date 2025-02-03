FROM python:alpine

#RUN apt-get update

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install django
#RUN  install -y python3-pip # Example package installation

COPY . /app 

     
# CMD [ "python","webapp/manage.py", "runserver","0.0.0.0:8000"]
