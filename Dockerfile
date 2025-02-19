FROM python:3.8

WORKDIR /code 

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 3000 

CMD ["python", "application.py"]
