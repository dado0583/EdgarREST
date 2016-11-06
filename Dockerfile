FROM python

RUN pip install pymongo
RUN pip install flask
RUN pip install flask-restplus
RUN pip install Flask-SQLAlchemy

COPY . /

CMD ["python3", "./rest_api_demo/app.py"]
