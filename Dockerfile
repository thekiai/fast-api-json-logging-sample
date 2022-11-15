FROM python:3.9-slim-buster
WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN apt update && \
    apt install -y libmariadb-dev-compat libmariadb-dev gcc && \
    pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./app /src/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]