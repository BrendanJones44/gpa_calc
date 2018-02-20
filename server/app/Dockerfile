FROM python:3.4
ADD . /gpa_calc
WORKDIR /gpa_calc
EXPOSE 5000
RUN app-get pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]