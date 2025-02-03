FROM python:alpine


WORKDIR /app

RUN pip install --upgrade pip

RUN pip install django

COPY . /app 

EXPOSE 8000

     
# CMD [ "python","webapp/manage.py", "runserver","0.0.0.0:8000"]
