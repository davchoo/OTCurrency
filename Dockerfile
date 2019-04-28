FROM python:3.7

WORKDIR /usr/src/OTCurrency

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "main:app"]