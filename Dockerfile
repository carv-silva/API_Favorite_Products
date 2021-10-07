FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir  /app
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD python manage.py makemigrations && python manage.py migrate
USER appuser

#COPY requirements.txt
#COPY . .

# ENTRYPOINT
# CMD
# https://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/