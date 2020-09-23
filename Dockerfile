
FROM python:latest

RUN pip install flask


COPY app.py /
RUN mkdir /templates
COPY templates/input.j2 /templates/input.j2
COPY templates/output.j2 /templates/output.j2

CMD python /app.py


