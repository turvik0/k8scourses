FROM python:3.12
WORKDIR /myservice
RUN pip install flask
RUN pip install requests
COPY service2.py ./
CMD ["python3", "service2.py"]