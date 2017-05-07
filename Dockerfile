FROM python:3.6.1

COPY . /code

WORKDIR /code
RUN pip3 install -r requirements.txt

EXPOSE 8080
CMD ["python", "optical/app.py"]