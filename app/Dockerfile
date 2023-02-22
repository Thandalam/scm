FROM python
WORKDIR .
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . .
EXPOSE 8000
CMD [ "uvicorn", "main:app", "--host", "127.0.0.1", "--port" ,"8000", "--reload" ]