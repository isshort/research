FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000
EXPOSE 3000
EXPOSE 5433
EXPOSE 6378
