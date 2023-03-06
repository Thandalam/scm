FROM python:3.9
WORKDIR /app/consumer
RUN pip install pymongo[srv]  kafka-python python-dotenv==0.19.2
COPY . .
# RUN pip install python-dotenv
# RUN pip install pymongo
CMD ["python3","consumer.py"]
