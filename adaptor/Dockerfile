FROM python

RUN mkdir /app

COPY adaptor.py /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["adaptor.py"]