FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app
COPY ./requirement.txt /app

WORKDIR /app

RUN pip install -r requirement.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]